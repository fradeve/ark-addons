# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'HelperCompoundsArea.feature'
        db.alter_column(u'appgeostat_helpercompoundsarea', 'feature_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appgeostat.HelperDitchesNumber'], unique=True, null=True))
        # Adding unique constraint on 'HelperCompoundsArea', fields ['feature']
        db.create_unique(u'appgeostat_helpercompoundsarea', ['feature_id'])


        # Changing field 'HelperCompoundsAccess.comp'
        db.alter_column(u'appgeostat_helpercompoundsaccess', 'comp_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['appgeostat.HelperCompoundsArea'], unique=True, null=True))
        # Adding unique constraint on 'HelperCompoundsAccess', fields ['comp']
        db.create_unique(u'appgeostat_helpercompoundsaccess', ['comp_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'HelperCompoundsAccess', fields ['comp']
        db.delete_unique(u'appgeostat_helpercompoundsaccess', ['comp_id'])

        # Removing unique constraint on 'HelperCompoundsArea', fields ['feature']
        db.delete_unique(u'appgeostat_helpercompoundsarea', ['feature_id'])


        # Changing field 'HelperCompoundsArea.feature'
        db.alter_column(u'appgeostat_helpercompoundsarea', 'feature_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appgeostat.HelperDitchesNumber'], null=True))

        # Changing field 'HelperCompoundsAccess.comp'
        db.alter_column(u'appgeostat_helpercompoundsaccess', 'comp_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['appgeostat.HelperCompoundsArea'], null=True))

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
        u'appgeostat.helpercompoundsaccess': {
            'Meta': {'object_name': 'HelperCompoundsAccess'},
            'comp': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['appgeostat.HelperCompoundsArea']", 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'orientation': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'poly': ('django.contrib.gis.db.models.fields.LineStringField', [], {'srid': '3857'}),
            'shapefile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appgeostat.Shapefile']"})
        },
        u'appgeostat.helpercompoundsarea': {
            'Meta': {'object_name': 'HelperCompoundsArea'},
            'feature': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['appgeostat.HelperDitchesNumber']", 'unique': 'True', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'open': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'poly': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '3857'}),
            'shapefile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appgeostat.Shapefile']"}),
            'storedarea': ('django.db.models.fields.FloatField', [], {'null': 'True'}),
            'type': ('django.db.models.fields.TextField', [], {'max_length': '255', 'null': 'True'})
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
            'poly': ('django.contrib.gis.db.models.fields.PolygonField', [], {'srid': '3857'}),
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
            'proj': ('django.db.models.fields.IntegerField', [], {'max_length': '6'}),
            'srs_wkt': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'stat_comp_acc': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stat_ditch_area': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stat_ditch_comp': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'stat_sett_area': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['appgeostat']