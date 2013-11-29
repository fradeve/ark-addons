# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'DateFieldsModel'
        db.create_table(u'stats_datefieldsmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'stats', ['DateFieldsModel'])

        # Adding model 'CxtModel'
        db.create_table(u'stats_cxtmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cxt', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
        ))
        db.send_create_signal(u'stats', ['CxtModel'])

        # Adding model 'TextFieldsModel'
        db.create_table(u'stats_textfieldsmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'stats', ['TextFieldsModel'])

        # Adding model 'FieldTypeModel'
        db.create_table(u'stats_fieldtypemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filetype', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal(u'stats', ['FieldTypeModel'])

        # Adding model 'ApiFieldsModel'
        db.create_table(u'stats_apifieldsmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.FieldTypeModel'], db_column='type')),
            ('cxt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.CxtModel'], db_column='cxt')),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
        ))
        db.send_create_signal(u'stats', ['ApiFieldsModel'])

        # Adding field 'StatsMapModel.fields'
        db.add_column(u'stats_statsmapmodel', 'fields',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.ApiFieldsModel'], null=True, db_column='fields'),
                      keep_default=False)

        # Adding field 'StatsMapModel.sitecode'
        db.add_column(u'stats_statsmapmodel', 'sitecode',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)

        # Adding field 'StatsProjectModel.maps'
        db.add_column(u'stats_statsprojectmodel', 'maps',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stats.StatsMapModel'], null=True, db_column='maps'),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'DateFieldsModel'
        db.delete_table(u'stats_datefieldsmodel')

        # Deleting model 'CxtModel'
        db.delete_table(u'stats_cxtmodel')

        # Deleting model 'TextFieldsModel'
        db.delete_table(u'stats_textfieldsmodel')

        # Deleting model 'FieldTypeModel'
        db.delete_table(u'stats_fieldtypemodel')

        # Deleting model 'ApiFieldsModel'
        db.delete_table(u'stats_apifieldsmodel')

        # Deleting field 'StatsMapModel.fields'
        db.delete_column(u'stats_statsmapmodel', 'fields')

        # Deleting field 'StatsMapModel.sitecode'
        db.delete_column(u'stats_statsmapmodel', 'sitecode')

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