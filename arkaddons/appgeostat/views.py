import datetime
import json
from django.conf import settings
from django.db.models import get_app, get_models
from django.http import HttpResponse
from django.shortcuts import redirect, render, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import GEOSGeometry            # general geometry
from django.contrib.gis.geos import Point, LineString, Polygon # base geometries
from django.contrib.gis.geos import MultiPolygon            # complex geometries
from django.views.generic import View, ListView, DeleteView, DetailView

from braces.views import LoginRequiredMixin

from vectorformats.Formats import Django, GeoJSON

from .models import Shapefile, Feature
from .models import HelperSettlementArea
from .models import HelperDitchesNumber
from .models import HelperCompoundsArea

from appgeostat import importer
from .forms import ImportShapefileForm
from .utils import get_geos_geometry
from .jenks import get_jenks_breaks
from .jenks import classify
from .trigonometry import get_round_vertex, check_nearest_point


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
                      {'form': form, 'err_msg': err_msg})


def context_results(shp_id):

    cur_shp = Shapefile.objects.get(id=shp_id)

    if cur_shp.helpersettlementarea_set.first() is None:
        settlement_area = None
    else:
        settlement_area = cur_shp.helpersettlementarea_set.first().storedarea

    results = {
        'settlement': {
            'settlement-area': {
                'display': 'Area',
                'value': settlement_area,
                'unit': 'sq_m',
                'actions_off': {
                    'request-ajax': {
                        'value': 'area'
                    }
                },
                'actions_on': {
                    'map': {
                        'table': 'helpersettlementarea',
                    }
                }
            }
        },
        'ditch': {
            'ditch-number': {
                'display': 'Number',
                'value': cur_shp.ditches_count(),
                'unit': '',
                'actions_off': {
                    'request-page': {
                        'link': 'href='+reverse('ditches_wizard', args=(shp_id,))
                    }
                },
                'actions_on': {
                    'edit': {
                        'link': 'href='+reverse('ditches_wizard', args=(shp_id,))
                    },
                    'map': {
                        'table': 'helperditchesnumber',
                        'filter': 'geojson&type=ditch',
                    }
                }
            },
            'perimeter': {
                'display': 'Perimeter',
                'value': cur_shp.ditches_perimeter(),
                'unit': 'm',
                'actions_off': {
                    'request-page': {
                        'link': 'href='+reverse('ditches_wizard', args=(shp_id,))
                    }
                },
                'actions_on': ''
            },
            'ditch-area': {
                'display': 'Area',
                'value': cur_shp.ditches_area(),
                'unit': 'sq_m',
                'actions_off': {
                    'request-ajax': {
                        'value': 'ditch-compound-area'
                    }
                },
                'actions_on': {
                    'map': {
                        'table': 'helpercompoundsarea',
                        'filter': 'geojson&type=ditch'
                    }
                }
            },
            'ditch-avg-area': {
                'display': 'AVG Area',
                'value': cur_shp.ditches_avg_area(),
                'unit': 'sq_m',
                'actions_off': '',
                'actions_on': '',
            }
        },
        'compound': {
            'compound-number': {
                'display': 'Number',
                'value': cur_shp.compounds_count(),
                'unit': '',
                'actions_off': {
                    'request-page': {
                        'link': 'href='+reverse('ditches_wizard', args=(shp_id,))
                    }
                },
                'actions_on': {
                    'edit': {
                        'link': 'href='+reverse('ditches_wizard', args=(shp_id,))
                    },
                    'map': {
                        'table': 'helperditchesnumber',
                        'filter': 'geojson&type=compound',
                    }
                }
            },
            'perimeter': {
                'display': 'Perimeter',
                'value': cur_shp.compounds_perimeter(),
                'unit': 'm',
                'actions_off': {
                    'request-page': {
                        'link': 'href='+reverse('ditches_wizard', args=(shp_id,))
                    }
                },
                'actions_on': ''
            },
            'compound-area': {
                'display': 'Area',
                'value': cur_shp.compounds_area(),
                'unit': 'sq_m',
                'actions_off': {
                    'request-ajax': {
                        'value': 'ditch-compound-area'
                    }
                },
                'actions_on': {
                    'map': {
                        'table': 'helpercompoundsarea',
                        'filter': 'geojson&type=compound',
                    }
                }
            },
            'compound-avg-area': {
                'display': 'AVG Area',
                'value': cur_shp.compounds_avg_area(),
                'unit': 'sq_m',
                'actions_off': '',
                'actions_on': '',
            }
        }
    }

    return results


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
        kwargs['general_context'] = context_results(curslug)

        return super(DetailShapefileView, self).get_context_data(**kwargs)


class AreaTemplateView(LoginRequiredMixin, View):

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

            context = context_results(cur_shp_id)
            return render_to_response(
                'appgeostat/shp_detail_table.html', {'context': context})


class DitchCompoundView(LoginRequiredMixin, View):
    """
    Differently from other stats views, this just checks values in the tables
    and calculates classes for each feature when started using AJAX POST. It is
    called by the Ditches Recognize Wizard before starting the guided procedure.
    """

    def post(self, request, *args, **kwargs):
        if request.is_ajax:

            cur_shp_id = kwargs['pk']

            # for each feature, get the perimeter and divide by classes
            # using perimeters for all the features in this layer.
            #
            # When we will use vectorlayers lib to get geoJSON with features
            # properties, we'll need to set the `geom` field. Having 2 different
            # fields to store polygons and multipolygons will generate problems,
            # so here we are storing polygons as multipolygons to use a single
            # field for all geometries.

            cur_shp = Shapefile.objects.get(id=cur_shp_id)

            # [A] check if features for this shp already exist in helper table
            if cur_shp.feature_set.count() == HelperDitchesNumber.objects\
                .filter(shapefile_id=cur_shp_id)\
                    .count():
                cur_feat = HelperDitchesNumber.objects.filter(
                    shapefile_id=cur_shp_id)
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
                        shapefile_id=cur_shp_id,
                        perimeter=feature.length)
                    new_feat.save()
                cur_feat = HelperDitchesNumber.objects.filter(
                    shapefile_id=cur_shp_id)

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
            Shapefile.objects.filter(id=cur_shp_id)\
                .update(jnb=jnb_classes_list)

            # [E] fill in the class for each feature of the helper layer
            for feature in cur_feat:
                class_val = classify(feature.perimeter, jnb_classes_list)
                feature.class_n = class_val
                feature.save()

            context = context_results(cur_shp_id)
            return render_to_response(
                'appgeostat/shp_detail_table.html', context)


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


class CompoundAreaTemplateView(LoginRequiredMixin, View):

    template_name = "appgeostat/shp_detail_table.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            cur_shp_id = kwargs['pk']

            error_msg = 'You need to distinguish ditches from' +\
                        ' compounds before generating internal' +\
                        ' areas. Use button in Number field.'

            # check if values for ditches and compounds have already been
            # calculated; if not, raise a warning in the interface
            results = context_results(cur_shp_id)
            if results['ditch']['ditch-number']['value'] is 0:
                if results['compound']['compound-number']['value'] is 0:
                    results['ditch']['ditch-area']['message'] =\
                        results['compound']['compound-area']['message'] = error_msg
            else:
                cur_shp = Shapefile.objects.get(id=cur_shp_id)
                cur_shp_geom = get_geos_geometry(cur_shp)
                cur_shp_geom.set_srid(4326)
                cur_shp_geom.transform(3857)

                for feature in cur_shp_geom:
                    area_points_list = []

                    # get geometry type from HelperDitchesNumber
                    cur_shp_type = HelperDitchesNumber.objects\
                        .filter(perimeter=feature.length)\
                        .first().type

                    # [A] get convex hull and its centroid
                    feat_convex_hull = feature.convex_hull
                    feat_centroid = feat_convex_hull.centroid

                    # [B] feature's hull farthest point from centroid
                    max_point = Point(
                        feat_convex_hull.extent[2],
                        feat_convex_hull.extent[3],
                        srid=3857)

                    radius = max_point.distance(feat_centroid)

                    # get vertexes in a circle (center=centroid), every n angle
                    vertexes_list = get_round_vertex(1, radius,
                                                     feat_centroid.x,
                                                     feat_centroid.y)

                    # for each point in vertex list
                    for point in vertexes_list:

                    # create new line between point and centroid
                        line = LineString(feat_centroid, point, srid=3857)
                        # line intersects geometry: get point nearest to centroid
                        intersection_line = line.intersection(feature)
                        if intersection_line.num_coords == 0:  # no intersection
                            pass
                        # intersection in 1 point
                        elif intersection_line.num_coords == 1:
                            area_points_list.append(Point(
                                intersection_line.coords[0]))
                        # intersection in 2 or more points
                        elif intersection_line.num_coords >= 2:
                            nearest_point = [None, 10000000]
                            # intersection generates a MultiLineString (> 2 pts)
                            if intersection_line.geom_type == 'MultiLineString':
                                for multiline_tuple in intersection_line.tuple:
                                    for coords_tuple in multiline_tuple:
                                        nearest_point = check_nearest_point(
                                            coords_tuple, 3857,
                                            feat_centroid,
                                            nearest_point)
                                area_points_list.append(nearest_point[0].tuple)
                            # intersection generates a LineString (2 pts)
                            else:
                                for coords_tuple in intersection_line.tuple:
                                    nearest_point = check_nearest_point(
                                        coords_tuple, 3857,
                                        feat_centroid,
                                        nearest_point)
                                area_points_list.append(nearest_point[0].tuple)

                    # close polygon and save convex hull of all points
                    if area_points_list.__len__() > 0:
                        area_points_list.append(area_points_list[0])
                    internal_area_polygon = Polygon(area_points_list, srid=3857)

                    internal_area_feature = HelperCompoundsArea(
                        shapefile_id=cur_shp_id,
                        poly=internal_area_polygon,
                        type=cur_shp_type,
                        storedarea=internal_area_polygon.area
                    )
                    internal_area_feature.save()

                results = context_results(cur_shp_id)

            return render_to_response(self.template_name, {'context': results})


class GetStatGeojsonView(LoginRequiredMixin, View):

    def post(self, request, *args, **kwargs):
        if request.is_ajax:

            if kwargs['field']:
                filter_field = kwargs['field']
                filter_value = kwargs['value']
            else:
                filter_field = None

            cur_shp_id = kwargs['pk']
            stat = kwargs['stat']
            table = request.POST.get('table')

            # iterate on helper models, select the one containing the statistics
            # we are interested in (according to parameters passed by AJAX POST)
            for model in get_models(get_app('appgeostat')):
                if 'helper' in model._meta.model_name:
                    if model._meta.model_name == table:
                        CurModel = model

            # create a geoJSON string from the result of the statistical geometry
            qs = CurModel.objects.filter(shapefile_id=cur_shp_id)

            # use a filter parameter to refine filter, if it has been passed
            if filter_field is not None:
                qs = qs.filter(**{filter_field: filter_value})

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
