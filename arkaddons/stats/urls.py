__appname__ = "stats"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from django.conf.urls import patterns, url

from stats.views import ManageProjectsView, StatsCreateView, StatsProjectView,\
    CheckApiStatusView, IndexView

urlpatterns = patterns('',
    # basic views
    url(r'^$', IndexView.as_view()),

    # projects management
    url(r'^projects/', ManageProjectsView.as_view()),
    url(r'^addproject/', StatsCreateView.as_view(), name='stats_create_view'),
    url(r'^project/(?P<slug>[^/]+)', StatsProjectView.as_view(), name="stats_detail_view"),
    url(r'^statuscheck/', CheckApiStatusView.as_view(), name="statuscheck"),
)