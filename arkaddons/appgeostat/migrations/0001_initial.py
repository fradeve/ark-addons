# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Shapefile'
        db.create_table(u'appgeostat_shapefile', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('filename', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('srs_wkt', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('geom_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('encoding', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('desc', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('dateadded', self.gf('django.db.models.fields.DateTimeField')(null=True)),
            ('classes', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('jnb', self.gf('django.db.models.fields.CharField')(max_length=500, null=True)),
            ('user_check_jnb', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'appgeostat', ['Shapefile'])

        # Adding model 'Attribute'
        db.create_table(u'appgeostat_attribute', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shapefile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appgeostat.Shapefile'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
            ('width', self.gf('django.db.models.fields.IntegerField')()),
            ('precision', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'appgeostat', ['Attribute'])

        # Adding model 'Feature'
        db.create_table(u'appgeostat_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shapefile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appgeostat.Shapefile'])),
            ('geom_point', self.gf('django.contrib.gis.db.models.fields.PointField')(null=True, blank=True)),
            ('geom_multipoint', self.gf('django.contrib.gis.db.models.fields.MultiPointField')(null=True, blank=True)),
            ('geom_multilinestring', self.gf('django.contrib.gis.db.models.fields.MultiLineStringField')(null=True, blank=True)),
            ('geom_multipolygon', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(null=True, blank=True)),
            ('geom_geometrycollection', self.gf('django.contrib.gis.db.models.fields.GeometryCollectionField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'appgeostat', ['Feature'])

        # Adding model 'AttributeValue'
        db.create_table(u'appgeostat_attributevalue', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appgeostat.Feature'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appgeostat.Attribute'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal(u'appgeostat', ['AttributeValue'])

        # Adding model 'HelperSettlementArea'
        db.create_table(u'appgeostat_helpersettlementarea', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shapefile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appgeostat.Shapefile'])),
            ('poly', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
            ('storedarea', self.gf('django.db.models.fields.FloatField')(null=True)),
        ))
        db.send_create_signal(u'appgeostat', ['HelperSettlementArea'])

        # Adding model 'HelperDitchesNumber'
        db.create_table(u'appgeostat_helperditchesnumber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('shapefile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appgeostat.Shapefile'])),
            ('poly', self.gf('django.contrib.gis.db.models.fields.MultiPolygonField')(srid=3857)),
            ('perimeter', self.gf('django.db.models.fields.FloatField')(null=True)),
            ('class_n', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('type', self.gf('django.db.models.fields.TextField')(max_length=255, null=True)),
        ))
        db.send_create_signal(u'appgeostat', ['HelperDitchesNumber'])


    def backwards(self, orm):
        # Deleting model 'Shapefile'
        db.delete_table(u'appgeostat_shapefile')

        # Deleting model 'Attribute'
        db.delete_table(u'appgeostat_attribute')

        # Deleting model 'Feature'
        db.delete_table(u'appgeostat_feature')

        # Deleting model 'AttributeValue'
        db.delete_table(u'appgeostat_attributevalue')

        # Deleting model 'HelperSettlementArea'
        db.delete_table(u'appgeostat_helpersettlementarea')

        # Deleting model 'HelperDitchesNumber'
        db.delete_table(u'appgeostat_helperditchesnumber')


    models = {
        u'appgeostat.attribute': {
            'Meta': {'object_name': 'Attribute'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'precision': ('django.db.models.fields.IntegerField', [], {}),
            'shapefile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appgeostat.Shapefile']"}),
            'type': ('django.db.models.fields.IntegerField', [], {}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        u'appgeostat.attributevalue': {
            'Meta': {'object_name': 'AttributeValue'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appgeostat.Attribute']"}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appgeostat.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'appgeostat.feature': {
            'Meta': {'object_name': 'Feature'},
            'geom_geometrycollection': ('django.contrib.gis.db.models.fields.GeometryCollectionField', [], {'null': 'True', 'blank': 'True'}),
            'geom_multilinestring': ('django.contrib.gis.db.models.fields.MultiLineStringField', [], {'null': 'True', 'blank': 'True'}),
            'geom_multipoint': ('django.contrib.gis.db.models.fields.MultiPointField', [], {'null': 'True', 'blank': 'True'}),
            'geom_multipolygon': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'null': 'True', 'blank': 'True'}),
            'geom_point': ('django.contrib.gis.db.models.fields.PointField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'shapefile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appgeostat.Shapefile']"})
        },
        u'appgeostat.helperditchesnumber': {
            'Meta': {'object_name': 'HelperDitchesNumber'},
            'class_n': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perimeter': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'poly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {'srid': '3857'}),
            'shapefile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appgeostat.Shapefile']"}),
            'type': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True'})
        },
        u'appgeostat.helpersettlementarea': {
            'Meta': {'object_name': 'HelperSettlementArea'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'poly': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'shapefile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appgeostat.Shapefile']"}),
            'storedarea': ('django.db.models.fields.FloatField', [], {'null': 'True'})
        },
        u'appgeostat.shapefile': {
            'Meta': {'object_name': 'Shapefile'},
            'classes': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'dateadded': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'desc': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'encoding': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'geom_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jnb': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True'}),
            'srs_wkt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'user_check_jnb': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['appgeostat']