__appname__ = "appgeostat"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = "0.1"

from django.conf.urls import patterns, url

from .views import import_shapefile, ListShapefileView, DetailShapefileView,\
    DeleteShapefileView, AreaTemplateView, GetStatGeojsonView,\
    DitchCompoundTemplateView

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

                       # get shapefile area
                       url(r'^(?P<pk>[^/]+)/area$',
                           AreaTemplateView.as_view(),
                           name='shape_area'),

                       # recognize shapefile's ditches/compounds
                       url(r'^(?P<pk>[^/]+)/number$',
                           DitchCompoundTemplateView.as_view(),
                           name='shape_rec_ditch_comp'),

                       # get geoJSON associated to a statistic
                       url(r'^(?P<pk>[^/]+)/(?P<stat>[^/]+)/geojson$',
                           GetStatGeojsonView.as_view(),
                           name='stat_geojson'),
                       )
