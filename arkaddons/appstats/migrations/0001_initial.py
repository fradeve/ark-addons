# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StatsMapModel'
        db.create_table(u'appstats_statsmapmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('dateget', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'appstats', ['StatsMapModel'])

        # Adding model 'StatsProjectModel'
        db.create_table(u'appstats_statsprojectmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('projectcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('projectname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('projectdesc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apiurl', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('apiuser', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('apipw', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appstats.StatsMapModel'], null=True, db_column='map')),
        ))
        db.send_create_signal(u'appstats', ['StatsProjectModel'])

        # Adding model 'CxtModel'
        db.create_table(u'appstats_cxtmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cxt', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appstats.StatsProjectModel'], null=True)),
        ))
        db.send_create_signal(u'appstats', ['CxtModel'])

        # Adding model 'FieldTypeModel'
        db.create_table(u'appstats_fieldtypemodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fieldtype', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
        ))
        db.send_create_signal(u'appstats', ['FieldTypeModel'])

        # Adding model 'TextFieldsModel'
        db.create_table(u'appstats_textfieldsmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cxt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appstats.CxtModel'], null=True, db_column='cxt')),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal(u'appstats', ['TextFieldsModel'])

        # Adding model 'DateFieldsModel'
        db.create_table(u'appstats_datefieldsmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('cxt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appstats.CxtModel'], null=True, db_column='cxt')),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'appstats', ['DateFieldsModel'])

        # Adding model 'ApiFieldsModel'
        db.create_table(u'appstats_apifieldsmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(max_length=250, null=True)),
            ('jsonfield', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appstats.FieldTypeModel'], db_column='type')),
            ('map', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appstats.StatsMapModel'], null=True)),
            ('cxt', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appstats.CxtModel'], null=True, blank=True)),
        ))
        db.send_create_signal(u'appstats', ['ApiFieldsModel'])


    def backwards(self, orm):
        # Deleting model 'StatsMapModel'
        db.delete_table(u'appstats_statsmapmodel')

        # Deleting model 'StatsProjectModel'
        db.delete_table(u'appstats_statsprojectmodel')

        # Deleting model 'CxtModel'
        db.delete_table(u'appstats_cxtmodel')

        # Deleting model 'FieldTypeModel'
        db.delete_table(u'appstats_fieldtypemodel')

        # Deleting model 'TextFieldsModel'
        db.delete_table(u'appstats_textfieldsmodel')

        # Deleting model 'DateFieldsModel'
        db.delete_table(u'appstats_datefieldsmodel')

        # Deleting model 'ApiFieldsModel'
        db.delete_table(u'appstats_apifieldsmodel')


    models = {
        u'appstats.apifieldsmodel': {
            'Meta': {'object_name': 'ApiFieldsModel'},
            'cxt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appstats.CxtModel']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jsonfield': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appstats.StatsMapModel']", 'null': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appstats.FieldTypeModel']", 'db_column': "'type'"})
        },
        u'appstats.cxtmodel': {
            'Meta': {'object_name': 'CxtModel'},
            'cxt': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appstats.StatsProjectModel']", 'null': 'True'})
        },
        u'appstats.datefieldsmodel': {
            'Meta': {'object_name': 'DateFieldsModel'},
            'cxt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appstats.CxtModel']", 'null': 'True', 'db_column': "'cxt'"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'appstats.fieldtypemodel': {
            'Meta': {'object_name': 'FieldTypeModel'},
            'fieldtype': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'appstats.statsmapmodel': {
            'Meta': {'object_name': 'StatsMapModel'},
            'dateget': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'appstats.statsprojectmodel': {
            'Meta': {'object_name': 'StatsProjectModel'},
            'apipw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'apiurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'apiuser': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'map': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appstats.StatsMapModel']", 'null': 'True', 'db_column': "'map'"}),
            'projectcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'projectdesc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'projectname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'appstats.textfieldsmodel': {
            'Meta': {'object_name': 'TextFieldsModel'},
            'cxt': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appstats.CxtModel']", 'null': 'True', 'db_column': "'cxt'"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['appstats']