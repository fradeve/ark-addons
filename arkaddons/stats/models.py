__appname__ = "stats"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from django.db import models


class StatsMapModel(models.Model):
    """Stores the maps to bind fields to each project"""
    dateget = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return '%s' % self.mapname


class StatsProjectModel(models.Model):
    """Stores statistics projects informations"""
    projectcode = models.CharField(max_length=10, blank=False, null=False,
                                   verbose_name="Project code")
    projectname = models.CharField(max_length=30,
                                   verbose_name="Project name")
    projectdesc = models.CharField(max_length=200,
                                   verbose_name="Project description")
    apiurl = models.URLField(null=True,
                             verbose_name="Archaeological data API URL")
    apiuser = models.CharField(max_length=100, blank=True, null=True,
                               verbose_name="API user")
    apipw = models.CharField(max_length=100, blank=True, null=True,
                             verbose_name="API password")
    map = models.ForeignKey(StatsMapModel, db_column='map', null=True)  # linked

    @models.permalink
    def get_absolute_url(self):
        return 'stats_detail_view', (), {'slug': self.projectcode}

    def get_field_list(self):
        """Generates a list of all the fields available for a certain map,
        or returns an empty list if no field has been defined."""
        fieldlist = {}
        try:
            for item in self.map.apifieldsmodel_set.values():
                fieldlist[item['key']] = item['jsonfield']
            return fieldlist
        except:  # FIXME: define more specific exception
            return fieldlist


class CxtModel(models.Model):
    """Stores the context list for a certain map"""
    cxt = models.CharField(max_length=50, blank=False, null=True)
    project = models.ForeignKey(StatsProjectModel, blank=False,
                                null=True)                              # linked


class FieldTypeModel(models.Model):
    fieldtype = models.CharField(max_length=10, blank=False, null=True)

    def __unicode__(self):
        return u'%s' % (self.fieldtype)


class TextFieldsModel(models.Model):
    """Stores all the text values for the imported fields"""
    cxt = models.ForeignKey(CxtModel, db_column='cxt', blank=False,
                            null=True)                                  # linked
    value = models.CharField(max_length=500, blank=True, null=True)


class DateFieldsModel(models.Model):
    cxt = models.ForeignKey(CxtModel, db_column='cxt', blank=False,
                            null=True)                                  # linked
    date = models.DateTimeField(blank=True, null=True)


class ApiFieldsModel(models.Model):
    """Stores info about the selected fields from API;
    Every map can have many ApiFields"""
    key = models.CharField(max_length=250, blank=False, null=True)
    jsonfield = models.CharField(max_length=250, blank=True, null=True)
    type = models.ForeignKey(FieldTypeModel, db_column='type')          # linked
    map = models.ForeignKey(StatsMapModel, blank=False, null=True)      # linked
    cxt = models.ForeignKey(CxtModel, blank=True, null=True)            # linked