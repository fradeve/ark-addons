__appname__ = "core"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from core.views import IndexView, ManageProjectsView, ArkCreateView, ArkProjectView,\
    CheckDbStatusView, CxtAllViewSet, RetrieveViewSet, CxtOneViewSet

admin.autodiscover()

router = DefaultRouter()
router.register(r'api', CxtOneViewSet)      # FIXME
router.register(r'api2', CxtAllViewSet)      # FIXME
router.register(r'api3', RetrieveViewSet)

urlpatterns = patterns('',
    # basic views
    url(r'^$', IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),

    # projects management
    url(r'^projects$', ManageProjectsView.as_view()),
    url(r'^statuscheck$', CheckDbStatusView.as_view(), name='statuscheck'),
    url(r'^addproject$', ArkCreateView.as_view(), name='ark_create_view'),
    url(r'^project/(?P<slug>[^/]+)$', ArkProjectView.as_view(), name='ark_detail_view'),

    # REST APIs
    url(r'^', include(router.urls)),

    # stats app
    (r'^stats/', include('stats.urls')),
)