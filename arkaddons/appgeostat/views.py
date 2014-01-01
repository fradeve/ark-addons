import datetime
import json
from django.conf import settings
from django.db.models import get_app, get_models
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon
from django.views.generic import View, ListView, DeleteView, DetailView

from braces.views import LoginRequiredMixin

from vectorformats.Formats import Django, GeoJSON

from appgeostat import importer
from utils import get_geos_geometry
from utils import get_jenks_breaks
from utils import classify

from .models import Shapefile, Feature, HelperSettlementArea,\
    HelperDitchesNumber
from .forms import ImportShapefileForm


@login_required
def import_shapefile(request):
    # If the page gets called, return the SHP load template
    if request.method == "GET":
        form = ImportShapefileForm()
        return render(request, "appgeostat/shp_upload.html",
                      {'form': form,
                       'err_msg': None})

    # If the template tries to POST to the page, start the import function
    elif request.method == "POST":
        form = ImportShapefileForm(request.POST,
                                   request.FILES)
        if form.is_valid():
            shapefile = request.FILES['import_file']
            encoding = request.POST['character_encoding']
            description = request.POST['description']
            dateadded = datetime.datetime.now()

            err_msg = importer.import_data(shapefile,
                                           encoding,
                                           description,
                                           dateadded)

            if err_msg is None:
                return redirect('shape_list')
        else:
            err_msg = None

        return render(request, "appgeostat/shp_upload.html",
                      {'form': form,
                       'err_msg': err_msg})


class ListShapefileView(LoginRequiredMixin, ListView):
    model = Shapefile
    template_name = "appgeostat/shp_list.html"
    context_object_name = 'shapes'


class DeleteShapefileView(LoginRequiredMixin, DeleteView):
    model = Shapefile
    success_url = reverse_lazy('shape_list')
    template_name = "appgeostat/shp_confirm_delete.html"


class DetailShapefileView(LoginRequiredMixin, DetailView):
    model = Shapefile
    template_name = "appgeostat/shp_detail.html"
    context_object_name = "shape"

    def get_context_data(self, **kwargs):
        """
        Get the features in geoJSON format using vectorformats library and
        passing it through context data kwargs. This is a way to insert features
        properties in geoJSON, directly from Feature model columns.
        """
        curslug = self.kwargs['pk']

        qs = Feature.objects.filter(shapefile_id=curslug)
        geoj = GeoJSON.GeoJSON()
        djf = Django.Django(
            geodjango="geom_multipolygon",
            properties=['shapefile_id'])
        kwargs['geojson'] = geoj.encode(djf.decode(qs))
        kwargs['style_base'] = settings.LAYERS_STYLES['base']
        kwargs['default_classes'] =\
            settings.GEOSTAT_SETTINGS['jenk_natural_breaks_classes']

        return super(DetailShapefileView, self).get_context_data(**kwargs)


class AreaTemplateView(LoginRequiredMixin, View):
    """
    Returns a single row template to be inserted in a table, with the data
    resulted from area calculation.
    """
    template_name = "appgeostat/shp_detail_tbl_row.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            cur_shp_id = kwargs['pk']

            # calculate area as GEOS object using convex hull operation,
            # save it, calculate area value, save it in db as geometry attribute
            cur_shp = Shapefile.objects.get(id=cur_shp_id)
            cur_shp_geom = get_geos_geometry(cur_shp)
            area_geom = GEOSGeometry(cur_shp_geom.convex_hull)

            # save the new GEOS area to geometry in db
            new_area = HelperSettlementArea(poly=area_geom,
                                            shapefile_id=cur_shp_id)
            new_area.save()

            # calculates the area and update the db entry
            area_geom.set_srid(4326)  # get measure in squared meters
            area_geom.transform(900913)  # ibidem
            HelperSettlementArea.objects.filter(
                shapefile_id=cur_shp_id)\
                .update(storedarea=area_geom.area)

            area_obj = HelperSettlementArea.objects.get(
                shapefile_id=cur_shp_id)

        data = {
            'status': 'success',
            'group': 'settlement',
            'value': 'Area',
            'result': area_obj.storedarea,
            'unit': 'sq_m',
            'geom': 'yes'
        }

        return render_to_response(self.template_name, data)


class DitchCompoundView(LoginRequiredMixin, View):
    """
    Differently from other stats views, this just checks values in the tables
    and calculates classes for each feature when started using AJAX POST. It is
    called by the Ditches Recognize Wizard before starting the guided procedure.
    """
    def dispatch(self, request, *args, **kwargs):
        self.cur_shp_id = kwargs['pk']
        return super(DitchCompoundView, self)\
            .dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax:

            # [1] layers with ditches and compounds:
            # for each feature, get the perimeter and divide by classes
            # using perimeters for all the features in this layer.
            #
            # When we will use vectorlayers lib to get geoJSON with features
            # properties, we'll need to set the `geom` field. Having 2 different
            # fields to store polygons and multipolygons will generate problems,
            # so here we are storing polygons as multipolygons to use a single
            # field for all geometries.

            # [2] layer with just compounds:
            # get the avg perimeters for all compounds and ditches in all
            # layers and try to assign class based on contextual data
            # [3] if contextual data not available (e.g. it is the first
            #     shapefile processed:
            # use as values avg perimeter of ditches and compounds defined
            # in settings

            cur_shp = Shapefile.objects.get(id=self.cur_shp_id)

            # [A] check if features for this shp already exist in helper table
            if cur_shp.feature_set.count() == HelperDitchesNumber.objects\
                .filter(shapefile_id=self.cur_shp_id)\
                    .count():
                cur_feat = HelperDitchesNumber.objects.filter(
                    shapefile_id=self.cur_shp_id)
            else:
                # create helping features and fill in perimeter for each
                cur_shp_geom = get_geos_geometry(cur_shp)
                cur_shp_geom.set_srid(4326)
                cur_shp_geom.transform(3857)
                for feature in cur_shp_geom:
                    if feature.geom_type == 'Polygon':
                        feature = MultiPolygon(feature)
                    new_feat = HelperDitchesNumber(
                        poly=feature,
                        shapefile_id=self.cur_shp_id,
                        perimeter=feature.length)
                    new_feat.save()
                cur_feat = HelperDitchesNumber.objects.filter(
                    shapefile_id=self.cur_shp_id)

            # [B] check if this shapefile has custom class number defined
            if cur_shp.classes:
                class_num = cur_shp.classes
            else:
                class_num = settings.GEOSTAT_SETTINGS['jenk_natural_breaks_classes']

            # [C] get all perimeters as list
            perimeters = cur_feat.values_list('perimeter', flat=True)
            perim_list = []
            for x in perimeters:
                perim_list.append(x)

            # [D] calculate Jenks Natural Breaks, save in shapefile and features
            jnb_classes_list = get_jenks_breaks(perim_list, int(class_num))
            Shapefile.objects.filter(id=self.cur_shp_id)\
                .update(jnb=jnb_classes_list)

            # [E] fill in the class for each feature of the helper layer
            for feature in cur_feat:
                class_val = classify(feature.perimeter, jnb_classes_list)
                feature.class_n = class_val
                feature.save()

            response = {'status': 'success'}

            return HttpResponse(json.dumps(response))


class SaveDefaultClassesView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            cur_shp_id = kwargs['pk']
            new_classes = request.POST.get('classes')
            Shapefile.objects.filter(id=cur_shp_id).update(classes=new_classes)

        return HttpResponse('success')


class SaveDitchesClassesView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            cur_shp_id = kwargs['pk']
            ditches_classes = self.request.POST.get('ditches').split()

            cur_features = HelperDitchesNumber.objects\
                .filter(shapefile_id=cur_shp_id)

            cur_features.update(type=None)  # clean type field

            for item in ditches_classes:  # write all ditches
                cur_features.filter(class_n=int(item)).update(type='ditch')

            cur_features.exclude(type='ditch').update(type='compound')

            return HttpResponse('success')


class GetStatGeojsonView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        if kwargs['field']:
            self.filter_field = kwargs['field']
            self.filter_value = kwargs['value']
        else:
            self.filter_field = None

        return super(GetStatGeojsonView, self) \
            .dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            cur_shp_id = kwargs['pk']
            stat = kwargs['stat']
            group = self.request.POST.get('group')

            cur_model_name = 'helper' + group + stat

            # iterate on helper models, select the one containing the statistics
            # we are interested in (according to parameters passed by AJAX POST)
            for model in get_models(get_app('appgeostat')):
                if 'helper' in model._meta.model_name:
                    if model._meta.model_name == cur_model_name:
                        CurModel = model

            # create a geoJSON string from the result of the statistical geometry
            qs = CurModel.objects.filter(shapefile_id=cur_shp_id)

            # use a filter parameter to refine filter, if it has been passed
            if self.filter_field is not None:
                qs = qs.filter(**{self.filter_field: self.filter_value})

            qs.transform()
            geoj = GeoJSON.GeoJSON()
            djf = Django.Django(
                geodjango="poly",
                properties=settings.LAYERS_STYLES[stat]['attributes'])
            stat_geom = geoj.encode(djf.decode(qs))

            response = {
                'geom': stat_geom,
                'style': settings.LAYERS_STYLES[stat]['style'],
                'palette': settings.LAYERS_STYLES[stat]['palette']
            }

            return HttpResponse(json.dumps(response))