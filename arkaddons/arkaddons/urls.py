from django.conf.urls import patterns, include, url
from core.views import IndexView, ManageProjectsView, ArkCreateView, ArkProjectView, CheckDbStatusView, CxtAllViewSet

from core import views
from rest_framework.routers import DefaultRouter

from django.contrib import admin

admin.autodiscover()

router = DefaultRouter()
router.register(r'api', CxtAllViewSet)

urlpatterns = patterns('',
    (r'^$', IndexView.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    (r'^projects', ManageProjectsView.as_view()),
    url(r'^statuscheck/', CheckDbStatusView.as_view(), name="statuscheck"),
    url(r'^addproject/', ArkCreateView.as_view(), name='ark_create_view'),
    url(r'^project/(?P<slug>[^/]+)', ArkProjectView.as_view(), name="ark_project_view"),
    url(r'^', include(router.urls)),
)
