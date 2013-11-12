from django.conf.urls import patterns, include, url
from core.views import IndexView, ManageProjectsView, ArkCreateView, ArkProjectView, ArkProjectEdit, checkdbstatus

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', IndexView.as_view()),
    (r'^projects', ManageProjectsView.as_view()),
    url(r'^statuscheck/', checkdbstatus),
    url(r'^addproject/', ArkCreateView.as_view(), name='ark_create_view'),
    url(r'^project/(?P<slug>[^/]+)', ArkProjectView.as_view(), name="ark_project_view"),
    url(r'^project/(?P<slug>[^/]+)/edit', ArkProjectEdit.as_view(), name="ark_project_edit"),
    #url(r'^project/(?P<slug>[^/]+)/import', ArkProjectImport.as_view()), #FIXME
    url(r'^admin/', include(admin.site.urls)),
    url(r'login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
)