# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StatsProjectModel'
        db.create_table(u'stats_statsprojectmodel', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('projectcode', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('projectname', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('projectdesc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('apiurl', self.gf('django.db.models.fields.URLField')(max_length=200, null=True)),
            ('apiuser', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('apipw', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'stats', ['StatsProjectModel'])


    def backwards(self, orm):
        # Deleting model 'StatsProjectModel'
        db.delete_table(u'stats_statsprojectmodel')


    models = {
        u'stats.statsprojectmodel': {
            'Meta': {'object_name': 'StatsProjectModel'},
            'apipw': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'apiurl': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True'}),
            'apiuser': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projectcode': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'projectdesc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'projectname': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['stats']