__appname__ = "stats"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from django.db import models


class StatsProjectModel(models.Model):
    """Stores statistics projects informations"""
    projectcode = models.CharField(max_length=10, blank=False, null=False, verbose_name="Project code")
    projectname = models.CharField(max_length=30, verbose_name="Project name")
    projectdesc = models.CharField(max_length=200, verbose_name="Project description")
    apiurl = models.URLField(null=True, verbose_name="Archaeological data API URL")
    apiuser = models.CharField(max_length=100, blank=True, null=True, verbose_name="API user")
    apipw = models.CharField(max_length=100, blank=True, null=True, verbose_name="API password")

    @models.permalink
    def get_absolute_url(self):
        return 'stats_detail_view', (), {'slug': self.projectcode}


class StatsMapModel(models.Model):
    """Stores the maps to bind fields to each project"""
    mapname = models.CharField(max_length=15, blank=False, null=False, verbose_name="Map name")
    mapdesc = models.CharField(max_length=100, blank=True, null=True, verbose_name="Map description")
