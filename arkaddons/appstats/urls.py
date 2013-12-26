__appname__ = "appstats"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from django.conf.urls import patterns, url

from appstats.views import ManageProjectsView, StatsCreateView, StatsProjectView,\
    CheckApiStatusView, IndexView, CreateFieldsView, SyncContextView

urlpatterns = patterns('',
                        # basic views
                        url(r'^$', IndexView.as_view()),

                        # projects
                        url(r'^projects$',
                            ManageProjectsView.as_view()),

                        # projects/add
                        url(r'^addproject$',
                            StatsCreateView.as_view(),
                            name='stats_create_view'),

                        # projects/details
                        url(r'^project/(?P<slug>[^/]+)$',
                            StatsProjectView.as_view(),
                            name='stats_detail_view'),

                        # projects/edit fields
                        url(r'^project/(?P<slug>[^/]+)/editmap$',
                            CreateFieldsView.as_view(),
                            name='stats_editmap_view'),

                        #url(r'^project/(?P<slug>[^/]+)/editmap/del/(?P<field>[^/]+)$',DelFieldView.as_view(), name="stats_delfield_view"),

                        # project/sync contexts
                        url(r'^project/(?P<slug>[^/]+)/synccxt$',
                            SyncContextView.as_view(),
                            name='stats_synccxt_view'),

                        # check API status
                        url(r'^statuscheck$',
                            CheckApiStatusView.as_view(),
                            name='statuscheck'),
)