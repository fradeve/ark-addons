import datetime
import json
from django.conf import settings
from django.db.models import get_app, get_models
from django.http import HttpResponse
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

        return super(DetailShapefileView, self).get_context_data(**kwargs)


class AreaTemplateView(LoginRequiredMixin, View):
    """
    Returns a single row template to be inserted in a table, with the data
    resulted from area calculation.
    """
    template_name = "appgeostat/shp_detail_tbl_row.html"

    def dispatch(self, request, *args, **kwargs):
        """Creates class-wide variable with current project ID"""
        self.cur_shp_id = kwargs['pk']
        return super(AreaTemplateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax():

            # if we have an area object associated to the current shapefile,
            # get the stored area value and the geoJSON
            if HelperSettlementArea.objects.filter(shapefile_id=self.cur_shp_id):
                area_obj = HelperSettlementArea.objects.get(
                    shapefile_id=self.cur_shp_id)

            else:
                # if we don't have any area object already in db, calculate it
                # as GEOS object, save geometry, calculate area and save it
                cur_shp = Shapefile.objects.get(id=self.cur_shp_id)
                cur_shp_geom = get_geos_geometry(cur_shp)
                area_geom = GEOSGeometry(cur_shp_geom.convex_hull)

                # save the new GEOS area to geometry in db
                new_area = HelperSettlementArea(poly=area_geom,
                                                shapefile_id=self.cur_shp_id)
                new_area.save()

                # calculates the area and update the db entry
                area_geom.set_srid(4326)  # get measure in squared meters
                area_geom.transform(900913)  # ibidem
                HelperSettlementArea.objects.filter(
                    shapefile_id=self.cur_shp_id)\
                    .update(storedarea=area_geom.area)

                area_obj = HelperSettlementArea.objects.get(
                    shapefile_id=self.cur_shp_id)

            data = {
                'status': 'success',
                'group': 'settlement',
                'value': 'Area',
                'result': area_obj.storedarea,
                'unit': 'sq_m',
                'geom': 'yes',
                'pk': self.cur_shp_id
            }

            return render_to_response(self.template_name, data)


class DitchCompoundTemplateView(LoginRequiredMixin, View):
    """
    Returns a single row template to be inserted in a table, with the data
    resulted from the calculation of ditches and compounds.
    """
    def dispatch(self, request, *args, **kwargs):
        self.cur_shp_id = kwargs['pk']
        return super(DitchCompoundTemplateView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        if request.is_ajax:

            if HelperDitchesNumber.objects.filter(type__isnull=True) is None:
                print('All features have a type attribute.')
                pass

            # [1] layers with ditches and compounds:
            # for each feature, get the perimeter and divide by classes
            # using perimeters for all the features in this layer.
            #
            # When we will use vectorlayers lib to get geoJSON with features
            # properties, we'll need to set the `geom` field. Having 2 different
            # fields to store polygons and multipolygons will generate problems,
            # so here we are storing polygons as multipolygons to use a single
            # field for all geometries.
            else:
                # [A] fill in perimeter value for each feature
                cur_shp_geom = get_geos_geometry(Shapefile.objects.get(
                    id=self.cur_shp_id))
                cur_shp_geom.set_srid(4326)
                cur_shp_geom.transform(900913)
                for feature in cur_shp_geom:
                    if feature.geom_type == 'Polygon':
                        feature = MultiPolygon(feature)
                    new_feat = HelperDitchesNumber(
                        poly=feature,
                        shapefile_id=self.cur_shp_id,
                        perimeter=feature.length)
                    new_feat.save()

                # [B] get all parameters as list
                perimeters = HelperDitchesNumber.objects.values_list(
                    'perimeter', flat=True)
                perim_list = []
                for x in perimeters:
                    perim_list.append(x)

                # [C] calculate Jenks Natural Breaks and save in Shapefile
                jnb = get_jenks_breaks(perim_list, 5)
                print(jnb)

            # [2] layer with just compounds:
            # get the avg perimeters for all compounds and ditches in all
            # layers and try to assign class based on contextual data
            # [3] if contextual data not available (e.g. it is the first
            #     shapefile processed:
            # use as values avg perimeter of ditches and compounds defined
            # in settings


class GetStatGeojsonView(LoginRequiredMixin, View):

    def post(self, context, **response_kwargs):
        self.cur_shp_id = self.request.POST.get('pk')
        self.stat = self.request.POST.get('stat')
        self.group = self.request.POST.get('group')

        cur_model_name = 'helper' + self.group + self.stat

        # iterate on helper models and select the one containing the statistics
        # we are interested in (according to parameters passed by AJAX POST)
        for model in get_models(get_app('appgeostat')):
            if 'helper' in model._meta.model_name:
                if model._meta.model_name == cur_model_name:
                    CurModel = model

        # create a geoJSON string from the result of the statistical geometry
        qs = CurModel.objects.filter(shapefile_id=self.cur_shp_id)
        geoj = GeoJSON.GeoJSON()
        djf = Django.Django(
            geodjango="poly",
            properties=settings.LAYERS_STYLES[self.stat]['attributes'])
        stat_geom = geoj.encode(djf.decode(qs))

        response = {
            'geom': stat_geom,
            'style': settings.LAYERS_STYLES[self.stat]['style']
        }

        return HttpResponse(json.dumps(response))