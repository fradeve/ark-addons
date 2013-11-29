# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ApiFieldsModel.jsonfield'
        db.add_column(u'stats_apifieldsmodel', 'jsonfield',
                      self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ApiFieldsModel.jsonfield'
        db.delete_column(u'stats_apifieldsmodel', 'jsonfield')


    models = {
        u'stats.apifieldsmodel': {
            'Meta': {'object_name': 'ApiFieldsModel'},
            'cxt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.CxtModel']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jsonfield': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.StatsMapModel']", 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.FieldTypeModel']", 'db_column': "'type'"})
        },
        u'stats.cxtmodel': {
            'Meta': {'object_name': 'CxtModel'},
            'cxt': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.StatsProjectModel']", 'null': 'True'})
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