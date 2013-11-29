# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'DateFieldsModel.cxt'
        db.add_column(u'stats_datefieldsmodel', 'cxt',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.CxtModel'], null=True, db_column='cxt'),
                      keep_default=False)

        # Adding field 'CxtModel.cxtcode'
        db.add_column(u'stats_cxtmodel', 'cxtcode',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)

        # Adding field 'TextFieldsModel.cxt'
        db.add_column(u'stats_textfieldsmodel', 'cxt',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.CxtModel'], null=True, db_column='cxt'),
                      keep_default=False)

        # Deleting field 'FieldTypeModel.filetype'
        db.delete_column(u'stats_fieldtypemodel', 'filetype')

        # Adding field 'FieldTypeModel.fieldtype'
        db.add_column(u'stats_fieldtypemodel', 'fieldtype',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True),
                      keep_default=False)

        # Deleting field 'StatsMapModel.sitecode'
        db.delete_column(u'stats_statsmapmodel', 'sitecode')

        # Deleting field 'StatsProjectModel.maps'
        db.delete_column(u'stats_statsprojectmodel', 'maps')

        # Adding field 'StatsProjectModel.map'
        db.add_column(u'stats_statsprojectmodel', 'map',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.StatsMapModel'], null=True, db_column='maps'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'DateFieldsModel.cxt'
        db.delete_column(u'stats_datefieldsmodel', 'cxt')

        # Deleting field 'CxtModel.cxtcode'
        db.delete_column(u'stats_cxtmodel', 'cxtcode')

        # Deleting field 'TextFieldsModel.cxt'
        db.delete_column(u'stats_textfieldsmodel', 'cxt')

        # Adding field 'FieldTypeModel.filetype'
        db.add_column(u'stats_fieldtypemodel', 'filetype',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 11, 25, 0, 0), max_length=10),
                      keep_default=False)

        # Deleting field 'FieldTypeModel.fieldtype'
        db.delete_column(u'stats_fieldtypemodel', 'fieldtype')

        # Adding field 'StatsMapModel.sitecode'
        db.add_column(u'stats_statsmapmodel', 'sitecode',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)

        # Adding field 'StatsProjectModel.maps'
        db.add_column(u'stats_statsprojectmodel', 'maps',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.StatsMapModel'], null=True, db_column='maps'),
                      keep_default=False)

        # Deleting field 'StatsProjectModel.map'
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
            'cxtcode': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stats.datefieldsmodel': {
            'Meta': {'object_name': 'DateFieldsModel'},
            'cxt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.CxtModel']", 'null': 'True', 'db_column': "'cxt'"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stats.fieldtypemodel': {
            'Meta': {'object_name': 'FieldTypeModel'},
            'fieldtype': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'stats.statsmapmodel': {
            'Meta': {'object_name': 'StatsMapModel'},
            'fields': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.ApiFieldsModel']", 'null': 'True', 'db_column': "'fields'"}),
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
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stats.StatsMapModel']", 'null': 'True', 'db_column': "'maps'"}),
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