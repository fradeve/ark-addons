# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ArkProjectModel'
        db.create_table(u'appcore_arkprojectmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('projectslug', self.gf('django.db.models.fields.SlugField')(max_length=30)),
            ('projectname', self.gf('django.db.models.fields.CharField')(max_length=25, null=True)),
            ('projectdesc', self.gf('django.db.models.fields.CharField')(max_length=150, null=True)),
            ('projectsitecode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('arkdbname', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('arkdbuser', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('arkdbpassword', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('arkdbhost', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('arkdbport', self.gf('django.db.models.fields.SmallIntegerField')(max_length=4, blank=True)),
            ('arkwfsaddress', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'appcore', ['ArkProjectModel'])


    def backwards(self, orm):
        # Deleting model 'ArkProjectModel'
        db.delete_table(u'appcore_arkprojectmodel')


    models = {
        u'appcore.arkprojectmodel': {
            'Meta': {'object_name': 'ArkProjectModel'},
            'arkdbhost': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True'}),
            'arkdbname': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'arkdbpassword': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'arkdbport': ('django.db.models.fields.SmallIntegerField', [], {'max_length': '4', 'blank': 'True'}),
            'arkdbuser': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True'}),
            'arkwfsaddress': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projectdesc': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True'}),
            'projectname': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True'}),
            'projectsitecode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'projectslug': ('django.db.models.fields.SlugField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['appcore']