__appname__ = "appgeostat"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = "0.1"

from django.conf.urls import patterns, url

# basic views
from .views import import_shapefile
from .views import ListShapefileView, DetailShapefileView, DeleteShapefileView
# views returning rendered HTML template
from .views import AreaTemplateView
from .views import DitchCompoundView
from .views import CompoundAreaTemplateView
from .views import CompoundAccessTemplateView
# views returning a geoJSON
from .views import GetStatGeojsonView
# views to save values in database
from .views import SaveDitchesClassesView, SaveDefaultClassesView

urlpatterns = patterns('',
                       # list all loaded SHPs
                       url(r'^$',
                           ListShapefileView.as_view(),
                           name='shape_list'),

                       # import SHPs: GET and POST refer to the same function
                       url(r'^import$',
                           import_shapefile,
                           name='shape_import'),

                       # details page
                       url(r'^(?P<pk>[^/]+)$',
                           DetailShapefileView.as_view(),
                           name='shape_detail'),

                       # delete shapefile
                       url(r'^(?P<pk>[^/]+)/delete$',
                           DeleteShapefileView.as_view(),
                           name='shape_delete'),

                       # [POST] get shapefile area
                       # returns: HTML, rendered template
                       url(r'^(?P<pk>[^/]+)/area$',
                           AreaTemplateView.as_view(),
                           name='shape_area'),

                       # [POST] recognize shapefile's ditches/compounds
                       # returns: HTML, rendered template
                       url(r'^(?P<pk>[^/]+)/number$',
                           DitchCompoundView.as_view(),
                           name='shape_rec_ditch_comp'),

                       # [POST] recognize shapefile's ditches/compounds areas
                       # returns: HTML, rendered template
                       url(r'^(?P<pk>[^/]+)/ditch-compound-area$',
                           CompoundAreaTemplateView.as_view(),
                           name='shape_comp_area'),

                       # [POST] recognize compound's access side
                       # returns: HTML, rendered template
                       url(r'^(?P<pk>[^/]+)/compound-access$',
                           CompoundAccessTemplateView.as_view(),
                           name='shape_comp_access'),

                       # wizard to recognize shapefile's ditches/compounds;
                       # same DetailView as above, with different template
                       url(r'^(?P<pk>[^/]+)/ditches-wizard$',
                           DetailShapefileView.as_view(
                               template_name='appgeostat/shp_classes_wizard.html'
                           ),
                           name='ditches_wizard'),

                       # [POST] save default classes number for this shapefile
                       # expects: classes
                       # returns: success
                       url(r'^(?P<pk>[^/]+)/number/default-classes$',
                           SaveDefaultClassesView.as_view(),
                           name='shape_save_default_class'),

                       # [POST] writes defined classes in features
                       # expects: ditches
                       # returns: success
                       url(r'^(?P<pk>[^/]+)/number/save-classes$',
                           SaveDitchesClassesView.as_view(),
                           name='shape_save_ditch_class'),

                       # [POST] get geoJSON associated to a statistic;
                       # optionally can filter against URL parameters `field` and `value`
                       # expects: table
                       # from URL: stat, field, value
                       # returns: geoJSON
                       url(r'^(?P<pk>[^/]+)/(?P<stat>[^/]+)/geojson(?:&(?P<field>[A-Za-z]+)=(?P<value>[A-Za-z]+))?$',
                           GetStatGeojsonView.as_view(),
                           name='stat_geojson'),
                       )
