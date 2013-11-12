# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ArkProjectModel'
        db.create_table(u'core_arkprojectmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('projectname', self.gf('django.db.models.fields.CharField')(max_length=15, null=True)),
            ('projectdesc', self.gf('django.db.models.fields.CharField')(max_length=150, null=True)),
            ('arkdbname', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('arkdbuser', self.gf('django.db.models.fields.CharField')(max_length=10, null=True)),
            ('arkdbpassword', self.gf('django.db.models.fields.CharField')(max_length=50, null=True)),
            ('arkdbhost', self.gf('django.db.models.fields.CharField')(max_length=30, null=True)),
            ('arkdbport', self.gf('django.db.models.fields.SmallIntegerField')(max_length=4, blank=True)),
        ))
        db.send_create_signal(u'core', ['ArkProjectModel'])


    def backwards(self, orm):
        # Deleting model 'ArkProjectModel'
        db.delete_table(u'core_arkprojectmodel')


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
            'projectname': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True'})
        }
    }

    complete_apps = ['core']