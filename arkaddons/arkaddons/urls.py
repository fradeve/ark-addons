__appname__ = "appcore"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from appcore.views import IndexView, ManageProjectsView,\
    ArkCreateView, ArkProjectView, CheckDbStatusView,\
    CxtAllViewSet, RetrieveViewSet, CxtOneViewSet

admin.autodiscover()

## /api/<projectid>/all
## /api/<projectid>/all?<attr>=<frag_type>
## /api/<projectid>/<cxtid>
## /api/<projectid>/<cxtid>?<attr>=<frag_type>

# explicitly binding ReadOnlyModelViewSets methods (list) to URLs
cxt_list = CxtAllViewSet.as_view({
    'get': 'list'
})

urlpatterns = patterns('',

    # APIs views
    url(
        r'^project/(?P<slug>[^/]+)/all$',
        cxt_list,
        name='cxt-list'),

    # basic views
    url(
        r'^$',
        IndexView.as_view()),

    url(
        r'^admin/',
        include(admin.site.urls)),

    url(
        r'login/$',
        'django.contrib.auth.views.login',
        {'template_name': 'login.html'}),

    url(
        r'logout/$',
        'django.contrib.auth.views.logout',
        {'next_page': '/'}),

    # projects management
    url(
        r'^projects$',
        ManageProjectsView.as_view()),

    url(
        r'^statuscheck$',
        CheckDbStatusView.as_view(),
        name='statuscheck'),

    url(
        r'^addproject$',
        ArkCreateView.as_view(),
        name='ark_create_view'),

    url(
        r'^project/(?P<slug>[^/]+)$',
        ArkProjectView.as_view(),
        name='ark_detail_view'),

    # appstats app
    (r'^stats/', include('appstats.urls')),
    # appgeostat app
    (r'^geostat/', include('appgeostat.urls')),
)