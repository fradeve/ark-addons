# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'ArkProjectModel.arkwfsaddress'
        db.add_column(u'core_arkprojectmodel', 'arkwfsaddress',
                      self.gf('django.db.models.fields.URLField')(max_length=200, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'ArkProjectModel.arkwfsaddress'
        db.delete_column(u'core_arkprojectmodel', 'arkwfsaddress')


    models = {
        u'core.arkprojectmodel': {
            'Meta': {'object_name': 'ArkProjectModel'},
            'arkdbhost': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'arkdbname': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'arkdbpassword': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'arkdbport': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4', 'blank': 'True'}),
            'arkdbuser': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'arkwfsaddress': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projectdesc': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'projectname': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'projectsitecode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'projectslug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['core']