# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'ArkProjectModel.projectid'
        db.delete_column(u'core_arkprojectmodel', 'projectid')

        # Adding field 'ArkProjectModel.projectslug'
        db.add_column(u'core_arkprojectmodel', 'projectslug',
                      self.gf('django.db.models.fields.SlugField')(default=datetime.datetime(2013, 11, 11, 0, 0), max_length=30),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'ArkProjectModel.projectid'
        db.add_column(u'core_arkprojectmodel', 'projectid',
                      self.gf('django.db.models.fields.CharField')(max_length=10, null=True),
                      keep_default=False)

        # Deleting field 'ArkProjectModel.projectslug'
        db.delete_column(u'core_arkprojectmodel', 'projectslug')


    models = {
        u'core.arkprojectmodel': {
            'Meta': {'object_name': 'ArkProjectModel'},
            'arkdbhost': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'arkdbname': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'arkdbpassword': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'arkdbport': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4', 'blank': 'True'}),
            'arkdbuser': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projectdesc': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'projectname': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'}),
            'projectslug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['core']