import datetime
import json
import csv
from django.conf import settings
from django.db.models import get_app, get_models
from django.http import HttpResponse
from django.shortcuts import redirect, render, render_to_response
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.gis.geos import GEOSGeometry                    # gener geom
from django.contrib.gis.geos import Point, LineString, Polygon      # base geoms
from django.contrib.gis.geos import MultiPolygon                    # more geoms
from django.contrib.gis.geos.error import GEOSException
from django.views.generic import View, ListView, DeleteView, DetailView
from django.core.exceptions import ObjectDoesNotExist

from braces.views import LoginRequiredMixin

from vectorformats.Formats import Django, GeoJSON

from .models import Shapefile, Feature
from .models import HelperSettlementArea
from .models import HelperDitchesNumber
from .models import HelperCompoundsArea
from .models import HelperCompoundsAccess

from appgeostat import importer
from .forms import ImportShapefileForm
from .utils import get_geos_geometry, get_side_dict
from .jenks import get_jenks_breaks
from .jenks import classify
from .trigonometry import get_round_vertex
from .trigonometry import check_nearest_point


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
            proj = request.POST['projection']
            dateadded = datetime.datetime.now()

            err_msg = importer.import_data(shapefile,
                                           encoding,
                                           description,
                                           proj,
                                           dateadded)

            if err_msg is None:
                return redirect('shape_list')
        else:
            err_msg = None

        return render(request, "appgeostat/shp_upload.html",
                      {'form': form, 'err_msg': err_msg})


def context_results(shp_id):
    """
    Returns the dictionary with the default values for the table to be
    generated by the Django template. Dict values could be replaced with
    updated values after a calculation and the new dict could be returned
    using render_to_response function.
    :param shp_id:
    :return:
    """

    cur_shp = Shapefile.objects.get(id=shp_id)

    # settlement / area
    def sett_area_status():
        if cur_shp.helpersettlementarea_set.first() is None:
            return None
        else:
            settlement_area = cur_shp.helpersettlementarea_set.first().storedarea
            return settlement_area

    # ditches / have been distinguished? do they exist?
    def ditch_status():
        if cur_shp.stat_ditch_comp is True:
            if cur_shp.ditches_count() == 0:
                return 'disabled'
            else:
                return
        else:
            return 'disabled'

    # compounds / have been distinguished? do they exist?
    def compound_status():
        if cur_shp.stat_ditch_comp is True:
            if cur_shp.compounds_count() == 0:
                return 'disabled'
            else:
                return
        else:
            return 'disabled'

    # compounds / if they exist, area geometries have been derived?
    def compound_area_status():
        if cur_shp.stat_ditch_area is True:
            return
        else:
            return 'disabled'

    results = {
        'settlement': {
            'settlement-area': {
                'display': 'Area',
                'value': sett_area_status(),
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
                        'link': 'href=' + reverse('ditches_wizard',
                                                  args=(shp_id,))
                    }
                },
                'actions_on': {
                    'edit': {
                        'link': 'href=' + reverse('ditches_wizard',
                                                  args=(shp_id,))
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
                        'status': ditch_status(),
                        'link': 'href=' + reverse('ditches_wizard',
                                                  args=(shp_id,))
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
                        'status': ditch_status(),
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
                        'link': 'href=' + reverse('ditches_wizard',
                                                  args=(shp_id,))
                    }
                },
                'actions_on': {
                    'edit': {
                        'link': 'href=' + reverse('ditches_wizard',
                                                  args=(shp_id,))
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
                        'status': compound_status(),
                        'link': 'href=' + reverse('ditches_wizard',
                                                  args=(shp_id,))
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
                        'status': compound_status(),
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
            },
            'compound-access': {
                'display': 'Access',
                'value': cur_shp.compounds_access_count(),
                'actions_off': {
                    'request-ajax': {
                        'status': compound_area_status(),
                        'value': 'compound-access'
                    }
                },
                'actions_on': {
                    'map': {
                        'table': 'helpercompoundsaccess'
                    },
                    'info': {
                        'position': 'top',
                        'title': 'Compounds orientation',
                        'content': cur_shp.compounds_access()
                    }
                }
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
        kwargs['default_classes'] = \
            settings.GEOSTAT_SETTINGS['jenk_natural_breaks_classes']
        kwargs['general_context'] = context_results(curslug)

        return super(DetailShapefileView, self).get_context_data(**kwargs)


class AreaTemplateView(LoginRequiredMixin, View):
    """
    Calculates settlement area, gets the updated dict with table rows and
    renders it with the table template, giving the updated table as a response.
    """

    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            cur_shp_id = kwargs['pk']

            # calculate area as GEOS object using convex hull operation,
            # save it, calculate area value, save it in db as geometry attribute
            cur_shp = Shapefile.objects.get(id=cur_shp_id)
            cur_shp_geom = get_geos_geometry(cur_shp)
            area_geom = GEOSGeometry(cur_shp_geom.convex_hull)

            # calculates the area and update the db entry
            area_geom.set_srid(4326)  # get measure in Google Mercator proj
            area_geom.transform(3857)  # ibidem

            # get area value in Shapefile's projection
            proj_area_geom = area_geom
            proj_area_geom.transform(cur_shp.proj)

            # save the new GEOS area to geometry in db
            new_area = HelperSettlementArea(shapefile_id=cur_shp_id,
                                            poly=area_geom,
                                            storedarea=proj_area_geom.area)
            new_area.save()

            cur_shp.stat_sett_area = True
            cur_shp.save()

            context = context_results(cur_shp_id)
            return render_to_response(
                'appgeostat/shp_detail_table.html', {'context': context})


class DitchCompoundView(LoginRequiredMixin, View):
    """
    For each feature, get the perimeter and divide by classes using perimeters
    for all the features in this layer. When we will use vectorlayers lib to get
    geoJSON with features properties, we'll need to set the `geom` field.
    Having 2 different fields to store polygons and multipolygons will generate
    problems, so here we are storing polygons as multipolygons to use a single
    field for all geometries.
    """

    def post(self, request, *args, **kwargs):
        if request.is_ajax:

            cur_shp_id = kwargs['pk']
            cur_shp = Shapefile.objects.get(id=cur_shp_id)

            # [A] check if features for this shp already exist in helper table
            if cur_shp.feature_set.count() == HelperDitchesNumber.objects \
                .filter(shapefile_id=cur_shp_id) \
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

                    # get perimeter in Shapefile's projection
                    proj_feature = feature
                    proj_feature.set_srid(cur_shp_geom.srid)
                    proj_feature.transform(cur_shp.proj)

                    new_feat = HelperDitchesNumber(
                        poly=feature,
                        shapefile_id=cur_shp_id,
                        perimeter=proj_feature.length)
                    new_feat.save()

                cur_shp.stat_ditch_comp = cur_shp.stat_ditch_comp = True
                cur_shp.save()

                cur_feat = HelperDitchesNumber.objects.filter(
                    shapefile_id=cur_shp_id)

            # [B] check if this shapefile has custom class number defined
            if cur_shp.classes:
                class_num = cur_shp.classes
            else:
                class_num = settings.GEOSTAT_SETTINGS[
                    'jenk_natural_breaks_classes']

            # [C] get all perimeters as list
            perimeters = cur_feat.values_list('perimeter', flat=True)
            perim_list = []
            for x in perimeters:
                perim_list.append(x)

            # [D] calculate Jenks Natural Breaks, save in shapefile and features
            jnb_classes_list = get_jenks_breaks(perim_list, int(class_num))
            Shapefile.objects.filter(id=cur_shp_id) \
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
    """
    Saves the classes values generated by JNB algorithm in the Shapefile model.
    """

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
            cur_shp = Shapefile.objects.get(id=cur_shp_id)
            ditches_classes = self.request.POST.get('ditches').split()

            cur_features = HelperDitchesNumber.objects \
                .filter(shapefile_id=cur_shp_id)

            cur_features.update(type=None)  # clean type field

            if ditches_classes is not None:
                for item in ditches_classes:  # write all ditches
                    cur_features.filter(class_n=int(item)).update(type='ditch')

            cur_features.exclude(type='ditch').update(type='compound')

            return HttpResponse('success')


class CompoundAreaTemplateView(LoginRequiredMixin, View):
    template_name = "appgeostat/shp_detail_table.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            cur_shp_id = kwargs['pk']
            cur_shp = Shapefile.objects.get(id=cur_shp_id)

            # check if the statistic has already been calculated
            if cur_shp.stat_ditch_area is True:
                pass
            else:
                cur_shp_geom = cur_shp.helperditchesnumber_set.all()

                for feature in cur_shp_geom:
                    # the list that will contains compound's area perimeter pts
                    area_points_list = []

                    # [A] get convex hull and its centroid
                    feat_convex_hull = feature.poly.convex_hull
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
                                                     feat_centroid.y,
                                                     3857)

                    # for each point in vertex list
                    for point in vertexes_list:

                    # create new line between point and centroid
                        line = LineString(feat_centroid, point, srid=3857)
                        # line intersects geometry: get point nearest to centroid
                        try:
                            intersection_line = line.intersection(feature.poly)
                        except GEOSException:
                            pass
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

                    # close polygon, get projected area and save
                    area_points_list.append(area_points_list[0])
                    internal_area_polygon = Polygon(area_points_list, srid=3857)

                    proj_area_polygon = internal_area_polygon
                    proj_area_polygon.transform(cur_shp.proj)

                    if feature.type == 'compound':
                        # recognize open/closed compound
                        tr = settings.GEOSTAT_SETTINGS['open_compound_treshold']
                        closed_limit = 360 - ((tr * 360) / 100)
                        if area_points_list.__len__() > closed_limit:
                            structure_open = False
                        else:
                            structure_open = True
                    else:
                        structure_open = None

                    internal_area_feature = HelperCompoundsArea(
                        shapefile_id=cur_shp_id,
                        feature=feature,
                        poly=internal_area_polygon,
                        perimeter=internal_area_polygon.length,
                        storedarea=proj_area_polygon.area,
                        type=feature.type,
                        open=structure_open
                    )
                    internal_area_feature.save()

                cur_shp.stat_ditch_area = True
                cur_shp.save()

            results = context_results(cur_shp_id)
            return render_to_response(self.template_name, {'context': results})


class CompoundAccessTemplateView(LoginRequiredMixin, View):
    template_name = "appgeostat/shp_detail_table.html"

    def post(self, request, *args, **kwargs):
        if request.is_ajax:
            cur_shp_id = kwargs['pk']
            cur_shp = Shapefile.objects.get(id=cur_shp_id)

            # check if values for ditches and compounds have already been
            # calculated; if not, raise a warning in the interface
            if cur_shp.stat_comp_acc:
                pass
            else:
                # iterate on all open compounds
                for compound in cur_shp.helpercompoundsarea_set \
                        .filter(type='compound', open=True):
                    # get sides and relative lengths as dictionary
                    sides = get_side_dict(compound, 3857)
                    # get longest side in area polygon as a LineString
                    access_linestr = max(sides, key=sides.get)

                    # get access lenght as projected value
                    proj_access_linestr = access_linestr
                    proj_access_linestr.transform(cur_shp.proj)

                    # get the centroid of the access side
                    feature_centroid = compound.poly.centroid

                    # get compound's farthest point from centroid
                    max_point = Point(compound.poly.convex_hull.extent[2],
                                      compound.poly.convex_hull.extent[3],
                                      srid=3857)
                    radius = max_point.distance(feature_centroid)

                    # draw cardinal points around the compound every 45 degree,
                    # and rotate them by 12 degree to align perpendicularly to N
                    cardinal_pts = get_round_vertex(
                        45,
                        radius,
                        feature_centroid.x,
                        feature_centroid.y,
                        3857,
                        12)

                    # create "cake slices" using cardinal points
                    polygon_list = []
                    for i, item in enumerate(cardinal_pts):
                        points = (feature_centroid.coords,
                                  item.coords,
                                  cardinal_pts[i - 1].coords,
                                  feature_centroid.coords)
                        polygon_list.append(Polygon(points, srid=3857))
                    sectors = MultiPolygon(polygon_list, srid=3857)

                    # get access side centroid
                    access_centroid = access_linestr.centroid
                    access_centroid.transform(3857)

                    # find sector containing the access centroid; get direction
                    for sector in sectors:
                        if sector.contains(access_centroid):
                            direction = sectors.index(sector)
                        else:
                            pass

                    # save the access LineString in a separate table
                    new_compound_access = HelperCompoundsAccess(
                        shapefile_id=cur_shp_id,
                        comp=compound,
                        poly=access_linestr,
                        length=proj_access_linestr.length,
                        orientation=direction
                    )
                    new_compound_access.save()

                cur_shp.stat_comp_acc = True
                cur_shp.save()

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


class ExportCsv(LoginRequiredMixin, DetailView):
    model = Shapefile

    def get(self, request, *args, **kwargs):
        cur_shp_id = self.kwargs['pk']

        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = \
            'attachment;filename="export_' + str(cur_shp_id) + '.csv"'
        writer = csv.writer(response)

        data = Shapefile.objects.get(id=cur_shp_id)\
            .helperditchesnumber_set\
            .all()\
            .order_by('type')

        writer.writerow([
            'shapefile-id',
            'struct-id',
            'struct-type',
            'struct-perim',
            'perim-class',
            'struct-area',
            'struct-area-perim',
            'struct-open',
            'access-length',
            'compound-orient'
        ])

        for feature in data:
            try:
                access_len = feature.helpercompoundsarea\
                    .helpercompoundsaccess.length
                access_orient = settings.GEOSTAT_SETTINGS['cardinals'][
                    feature.helpercompoundsarea
                    .helpercompoundsaccess.orientation]
            except ObjectDoesNotExist:
                access_len = access_orient = ''

            writer.writerow([
                feature.shapefile_id,
                feature.id,
                feature.type,
                feature.perimeter,
                feature.class_n,
                feature.helpercompoundsarea.storedarea,
                feature.helpercompoundsarea.perimeter,
                feature.helpercompoundsarea.open,
                access_len,
                access_orient
            ])

        return response