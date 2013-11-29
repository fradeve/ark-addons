# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CxtModel.fields'
        db.add_column(u'stats_cxtmodel', 'fields',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.ApiFieldsModel'], null=True),
                      keep_default=False)

        # Deleting field 'ApiFieldsModel.cxt'
        db.delete_column(u'stats_apifieldsmodel', 'cxt')


    def backwards(self, orm):
        # Deleting field 'CxtModel.fields'
        db.delete_column(u'stats_cxtmodel', 'fields_id')


        # User chose to not deal with backwards NULL issues for 'ApiFieldsModel.cxt'
        raise RuntimeError("Cannot reverse this migration. 'ApiFieldsModel.cxt' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'ApiFieldsModel.cxt'
        db.add_column(u'stats_apifieldsmodel', 'cxt',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.CxtModel'], db_column='cxt'),
                      keep_default=False)


    models = {
        u'stats.apifieldsmodel': {
            'Meta': {'object_name': 'ApiFieldsModel'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.StatsMapModel']", 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.FieldTypeModel']", 'db_column': "'type'"})
        },
        u'stats.cxtmodel': {
            'Meta': {'object_name': 'CxtModel'},
            'cxt': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'cxtcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'fields': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.ApiFieldsModel']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stats.datefieldsmodel': {
            'Meta': {'object_name': 'DateFieldsModel'},
            'cxt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.CxtModel']", 'null': 'True', 'db_column': "'cxt'"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stats.fieldtypemodel': {
            'Meta': {'object_name': 'FieldTypeModel'},
            'fieldtype': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stats.statsmapmodel': {
            'Meta': {'object_name': 'StatsMapModel'},
            'dateget': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mapdesc': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mapname': ('django.db.models.fields.CharField', [], {'max_length': '15'})
        },
        u'stats.statsprojectmodel': {
            'Meta': {'object_name': 'StatsProjectModel'},
            'apipw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'apiurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'apiuser': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.StatsMapModel']", 'null': 'True', 'db_column': "'map'"}),
            'projectcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'projectdesc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'projectname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'stats.textfieldsmodel': {
            'Meta': {'object_name': 'TextFieldsModel'},
            'cxt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.CxtModel']", 'null': 'True', 'db_column': "'cxt'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['stats']