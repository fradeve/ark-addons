# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'StatsMapModel.project'
        db.delete_column(u'stats_statsmapmodel', 'project')

        # Adding field 'StatsProjectModel.maps'
        db.add_column(u'stats_statsprojectmodel', 'maps',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.StatsMapModel'], null=True, db_column='maps'),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'StatsMapModel.project'
        db.add_column(u'stats_statsmapmodel', 'project',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.StatsProjectModel'], null=True, db_column='project'),
                      keep_default=False)

        # Deleting field 'StatsProjectModel.maps'
        db.delete_column(u'stats_statsprojectmodel', 'maps')


    models = {
        u'stats.apifieldsmodel': {
            'Meta': {'object_name': 'ApiFieldsModel'},
            'cxt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.CxtModel']", 'db_column': "'cxt'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.FieldTypeModel']", 'db_column': "'type'"})
        },
        u'stats.cxtmodel': {
            'Meta': {'object_name': 'CxtModel'},
            'cxt': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stats.datefieldsmodel': {
            'Meta': {'object_name': 'DateFieldsModel'},
            'date': ('django.db.models.fields.DateTimeField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stats.fieldtypemodel': {
            'Meta': {'object_name': 'FieldTypeModel'},
            'filetype': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stats.statsmapmodel': {
            'Meta': {'object_name': 'StatsMapModel'},
            'fields': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.ApiFieldsModel']", 'null': 'True', 'db_column': "'fields'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapdesc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mapname': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'sitecode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'})
        },
        u'stats.statsprojectmodel': {
            'Meta': {'object_name': 'StatsProjectModel'},
            'apipw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'apiurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'apiuser': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'maps': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.StatsMapModel']", 'null': 'True', 'db_column': "'maps'"}),
            'projectcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'projectdesc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'projectname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'stats.textfieldsmodel': {
            'Meta': {'object_name': 'TextFieldsModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stats']