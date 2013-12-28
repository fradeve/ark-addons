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
        u'appcore.abklutabktype': {
            'Meta': {'object_name': 'AbkLutAbktype', 'db_table': "u'abk_lut_abktype'", 'managed': 'False'},
            'abktype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.abktblabk': {
            'Meta': {'object_name': 'AbkTblAbk', 'db_table': "u'abk_tbl_abk'", 'managed': 'False'},
            'abk_cd': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'abk_no': ('django.db.models.fields.IntegerField', [], {}),
            'abktype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.AbkLutAbktype']", 'db_column': "u'abktype'"}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'ste_cd': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'appcore.aeltblael': {
            'Meta': {'object_name': 'AelTblAel', 'db_table': "u'ael_tbl_ael'", 'managed': 'False'},
            'ael_cd': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'ael_no': ('django.db.models.fields.IntegerField', [], {}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'ste_cd': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
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
        },
        u'appcore.cnstblcns': {
            'Meta': {'object_name': 'CnsTblCns', 'db_table': "u'cns_tbl_cns'", 'managed': 'False'},
            'cns_cd': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'cns_no': ('django.db.models.fields.IntegerField', [], {}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'ste_cd': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'appcore.corlutactiontype': {
            'Meta': {'object_name': 'CorLutActiontype', 'db_table': "u'cor_lut_actiontype'", 'managed': 'False'},
            'actiontype': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'appcore.corlutaliastype': {
            'Meta': {'object_name': 'CorLutAliastype', 'db_table': "u'cor_lut_aliastype'", 'managed': 'False'},
            'aliastype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.corlutattribute': {
            'Meta': {'object_name': 'CorLutAttribute', 'db_table': "u'cor_lut_attribute'", 'managed': 'False'},
            'attribute': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'attributetype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutAttributetype']", 'db_column': "u'attributetype'"}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'appcore.corlutattributetype': {
            'Meta': {'object_name': 'CorLutAttributetype', 'db_table': "u'cor_lut_attributetype'", 'managed': 'False'},
            'attributetype': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'appcore.corlutdatetype': {
            'Meta': {'object_name': 'CorLutDatetype', 'db_table': "u'cor_lut_datetype'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'datetype': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'appcore.corlutfile': {
            'Meta': {'object_name': 'CorLutFile', 'db_table': "u'cor_lut_file'", 'managed': 'False'},
            'batch': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'filename': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'filetype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutFiletype']", 'db_column': "u'filetype'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'uri': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        u'appcore.corlutfiletype': {
            'Meta': {'object_name': 'CorLutFiletype', 'db_table': "u'cor_lut_filetype'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'filetype': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.corlutlanguage': {
            'Meta': {'object_name': 'CorLutLanguage', 'db_table': "u'cor_lut_language'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'appcore.corlutnumbertype': {
            'Meta': {'object_name': 'CorLutNumbertype', 'db_table': "u'cor_lut_numbertype'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'numbertype': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'qualifier': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'appcore.corlutspanlabel': {
            'Meta': {'object_name': 'CorLutSpanlabel', 'db_table': "u'cor_lut_spanlabel'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'spanlabel': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'spantype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutSpantype']", 'db_column': "u'spantype'"}),
            'typemod': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'appcore.corlutspantype': {
            'Meta': {'object_name': 'CorLutSpantype', 'db_table': "u'cor_lut_spantype'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'evaluation': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {}),
            'spantype': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'appcore.corluttxttype': {
            'Meta': {'object_name': 'CorLutTxttype', 'db_table': "u'cor_lut_txttype'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'module': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'txttype': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'appcore.corlvuapplications': {
            'Meta': {'object_name': 'CorLvuApplications', 'db_table': "u'cor_lvu_applications'", 'managed': 'False'},
            'application_define_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'application_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'appcore.corlvuapplicationsseq': {
            'Meta': {'object_name': 'CorLvuApplicationsSeq', 'db_table': "u'cor_lvu_applications_seq'", 'managed': 'False'},
            'sequence': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.corlvuareaadminareas': {
            'Meta': {'object_name': 'CorLvuAreaAdminAreas', 'db_table': "u'cor_lvu_area_admin_areas'", 'managed': 'False'},
            'area_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perm_user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvuareas': {
            'Meta': {'object_name': 'CorLvuAreas', 'db_table': "u'cor_lvu_areas'", 'managed': 'False'},
            'application_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_define_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'area_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'appcore.corlvuareasseq': {
            'Meta': {'object_name': 'CorLvuAreasSeq', 'db_table': "u'cor_lvu_areas_seq'", 'managed': 'False'},
            'sequence': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.corlvugrouprights': {
            'Meta': {'object_name': 'CorLvuGrouprights', 'db_table': "u'cor_lvu_grouprights'", 'managed': 'False'},
            'group_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'right_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'right_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvugroups': {
            'Meta': {'object_name': 'CorLvuGroups', 'db_table': "u'cor_lvu_groups'", 'managed': 'False'},
            'group_define_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'group_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'group_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'owner_group_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'owner_user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvugroupsseq': {
            'Meta': {'object_name': 'CorLvuGroupsSeq', 'db_table': "u'cor_lvu_groups_seq'", 'managed': 'False'},
            'sequence': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.corlvugroupsubgroups': {
            'Meta': {'object_name': 'CorLvuGroupSubgroups', 'db_table': "u'cor_lvu_group_subgroups'", 'managed': 'False'},
            'group_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subgroup_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvugroupusers': {
            'Meta': {'object_name': 'CorLvuGroupusers', 'db_table': "u'cor_lvu_groupusers'", 'managed': 'False'},
            'group_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perm_user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvupermusers': {
            'Meta': {'object_name': 'CorLvuPermUsers', 'db_table': "u'cor_lvu_perm_users'", 'managed': 'False'},
            'auth_container_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'auth_user_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perm_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'perm_user_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvupermusersseq': {
            'Meta': {'object_name': 'CorLvuPermUsersSeq', 'db_table': "u'cor_lvu_perm_users_seq'", 'managed': 'False'},
            'sequence': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.corlvurightimplied': {
            'Meta': {'object_name': 'CorLvuRightImplied', 'db_table': "u'cor_lvu_right_implied'", 'managed': 'False'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'implied_right_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'right_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvurights': {
            'Meta': {'object_name': 'CorLvuRights', 'db_table': "u'cor_lvu_rights'", 'managed': 'False'},
            'area_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'has_implied': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'right_define_name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'right_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvurightsseq': {
            'Meta': {'object_name': 'CorLvuRightsSeq', 'db_table': "u'cor_lvu_rights_seq'", 'managed': 'False'},
            'sequence': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.corlvutranslations': {
            'Meta': {'object_name': 'CorLvuTranslations', 'db_table': "u'cor_lvu_translations'", 'managed': 'False'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            'section_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'section_type': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'translation_id': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvutranslationsseq': {
            'Meta': {'object_name': 'CorLvuTranslationsSeq', 'db_table': "u'cor_lvu_translations_seq'", 'managed': 'False'},
            'sequence': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.corlvuuserrights': {
            'Meta': {'object_name': 'CorLvuUserrights', 'db_table': "u'cor_lvu_userrights'", 'managed': 'False'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'perm_user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'right_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'right_level': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'appcore.corlvuusers': {
            'Meta': {'object_name': 'CorLvuUsers', 'db_table': "u'cor_lvu_users'", 'managed': 'False'},
            'auth_user_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32', 'blank': 'True'}),
            'handle': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'lastlogin': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'owner_group_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'owner_user_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'passwd': ('django.db.models.fields.CharField', [], {'max_length': '32', 'blank': 'True'})
        },
        u'appcore.corlvuusersseq': {
            'Meta': {'object_name': 'CorLvuUsersSeq', 'db_table': "u'cor_lvu_users_seq'", 'managed': 'False'},
            'sequence': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.cortblaction': {
            'Meta': {'object_name': 'CorTblAction', 'db_table': "u'cor_tbl_action'", 'managed': 'False'},
            'actiontype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutActiontype']", 'db_column': "u'actiontype'"}),
            'actor_itemkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'actor_itemvalue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.AbkTblAbk']", 'db_column': "u'actor_itemvalue'"}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'itemvalue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CxtTblCxt']", 'db_column': "u'itemvalue'"})
        },
        u'appcore.cortblalias': {
            'Meta': {'object_name': 'CorTblAlias', 'db_table': "u'cor_tbl_alias'", 'managed': 'False'},
            'alias': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'aliastype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutAliastype']", 'db_column': "u'aliastype'"}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'itemvalue': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'appcore.cortblattribute': {
            'Meta': {'object_name': 'CorTblAttribute', 'db_table': "u'cor_tbl_attribute'", 'managed': 'False'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutAttribute']", 'db_column': "u'attribute'"}),
            'boolean': ('django.db.models.fields.IntegerField', [], {}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'itemvalue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'frag_attrs'", 'db_column': "u'itemvalue'", 'to': u"orm['appcore.CxtTblCxt']"})
        },
        u'appcore.cortblcmap': {
            'Meta': {'object_name': 'CorTblCmap', 'db_table': "u'cor_tbl_cmap'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'import_cre_by': ('django.db.models.fields.IntegerField', [], {}),
            'import_cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'nname': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'sourcedb': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'stecd': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'appcore.cortblcmapdata': {
            'Meta': {'object_name': 'CorTblCmapData', 'db_table': "u'cor_tbl_cmap_data'", 'managed': 'False'},
            'cmap': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'cre_by': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'mapto_id': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'mapto_tbl': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sourcedata': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sourcelocation': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'appcore.cortblcmapstructure': {
            'Meta': {'object_name': 'CorTblCmapStructure', 'db_table': "u'cor_tbl_cmap_structure'", 'managed': 'False'},
            'ark_mod': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'class_field': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_column': "u'class'"}),
            'cmap': ('django.db.models.fields.IntegerField', [], {}),
            'col': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'end_source_col': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'false': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'lang': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'log': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'lut_idcol': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lut_tbl': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'lut_valcol': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'notset': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'raw_itemval_col': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'raw_itemval_join_col': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'raw_itemval_tbl': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'raw_stecd_col': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'raw_stecd_join_col': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'raw_stecd_tbl': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tbl': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tbl_itemval_join_col': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tbl_stecd_join_col': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'true': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'uid_col': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'xmi_itemkey': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'xmi_itemval_col': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'appcore.cortblcol': {
            'Meta': {'object_name': 'CorTblCol', 'db_table': "u'cor_tbl_col'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'dbname': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.cortbldate': {
            'Meta': {'object_name': 'CorTblDate', 'db_table': "u'cor_tbl_date'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'datefield': ('django.db.models.fields.DateTimeField', [], {'db_column': "u'date'"}),
            'datetype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutDatetype']", 'db_column': "u'datetype'"}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'itemvalue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'frag_date'", 'db_column': "u'itemvalue'", 'to': u"orm['appcore.CxtTblCxt']"})
        },
        u'appcore.cortblfile': {
            'Meta': {'object_name': 'CorTblFile', 'db_table': "u'cor_tbl_file'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'file': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'itemvalue': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'appcore.cortblfilter': {
            'Meta': {'object_name': 'CorTblFilter', 'db_table': "u'cor_tbl_filter'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'filter': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sgrp': ('django.db.models.fields.IntegerField', [], {}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '6'})
        },
        u'appcore.cortbllog': {
            'Meta': {'object_name': 'CorTblLog', 'db_table': "u'cor_tbl_log'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'refid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'vars': ('django.db.models.fields.TextField', [], {})
        },
        u'appcore.cortblmarkup': {
            'Meta': {'object_name': 'CorTblMarkup', 'db_table': "u'cor_tbl_markup'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'markup': ('django.db.models.fields.TextField', [], {}),
            'mod_short': ('django.db.models.fields.TextField', [], {}),
            'nname': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'appcore.cortblmodule': {
            'Meta': {'object_name': 'CorTblModule', 'db_table': "u'cor_tbl_module'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'shortform': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'appcore.cortblnumber': {
            'Meta': {'object_name': 'CorTblNumber', 'db_table': "u'cor_tbl_number'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'fragid': ('django.db.models.fields.IntegerField', [], {}),
            'fragtype': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'itemvalue': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'number': ('django.db.models.fields.FloatField', [], {}),
            'numbertype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutNumbertype']", 'db_column': "u'numbertype'"}),
            'typemod': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'appcore.cortblsgrp': {
            'Meta': {'object_name': 'CorTblSgrp', 'db_table': "u'cor_tbl_sgrp'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'sgrp': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'appcore.cortblspan': {
            'Meta': {'object_name': 'CorTblSpan', 'db_table': "u'cor_tbl_span'", 'managed': 'False'},
            'beg': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'end': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'itemvalue': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'spantype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutSpantype']", 'db_column': "u'spantype'"}),
            'typemod': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        u'appcore.cortblspanattr': {
            'Meta': {'object_name': 'CorTblSpanattr', 'db_table': "u'cor_tbl_spanattr'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'span': ('django.db.models.fields.IntegerField', [], {}),
            'spanlabel': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutSpanlabel']", 'db_column': "u'spanlabel'"})
        },
        u'appcore.cortblste': {
            'Meta': {'object_name': 'CorTblSte', 'db_table': "u'cor_tbl_ste'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.CharField', [], {'max_length': '10', 'primary_key': 'True'})
        },
        u'appcore.cortbltxt': {
            'Meta': {'object_name': 'CorTblTxt', 'db_table': "u'cor_tbl_txt'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'itemvalue': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "u'frag_txt'", 'db_column': "u'itemvalue'", 'to': u"orm['appcore.CxtTblCxt']"}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'txt': ('django.db.models.fields.TextField', [], {}),
            'txttype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorLutTxttype']", 'db_column': "u'txttype'"})
        },
        u'appcore.cortblusers': {
            'Meta': {'object_name': 'CorTblUsers', 'db_table': "u'cor_tbl_users'", 'managed': 'False'},
            'account_enabled': ('django.db.models.fields.IntegerField', [], {}),
            'cre_by': ('django.db.models.fields.IntegerField', [], {}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'firstname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'initials': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '10', 'blank': 'True'}),
            'lastname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'sfilter': ('django.db.models.fields.IntegerField', [], {}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'appcore.cortblwmc': {
            'Meta': {'object_name': 'CorTblWmc', 'db_table': "u'cor_tbl_wmc'", 'managed': 'False'},
            'comments': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'extents': ('django.db.models.fields.TextField', [], {}),
            'gmap_api_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'legend_array': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'osm': ('django.db.models.fields.IntegerField', [], {'db_column': "u'OSM'"}),
            'projection': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'public': ('django.db.models.fields.IntegerField', [], {}),
            'scales': ('django.db.models.fields.TextField', [], {}),
            'wmc': ('django.db.models.fields.TextField', [], {}),
            'zoom': ('django.db.models.fields.IntegerField', [], {})
        },
        u'appcore.cortblwwwpages': {
            'Meta': {'object_name': 'CorTblWwwpages', 'db_table': "u'cor_tbl_wwwpages'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'defaultvars': ('django.db.models.fields.TextField', [], {}),
            'file': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'navlinkvars': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'navname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sgrp': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sortposs': ('django.db.models.fields.IntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'appcore.cortblxmi': {
            'Meta': {'object_name': 'CorTblXmi', 'db_table': "u'cor_tbl_xmi'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'itemkey': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'itemvalue': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'xmi_itemkey': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'xmi_itemvalue': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'appcore.cxtlutcxttype': {
            'Meta': {'object_name': 'CxtLutCxttype', 'db_table': "u'cxt_lut_cxttype'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'cxttype': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'})
        },
        u'appcore.cxttblcxt': {
            'Meta': {'object_name': 'CxtTblCxt', 'db_table': "u'cxt_tbl_cxt'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']", 'db_column': "u'cre_by'"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'cxt_cd': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'cxt_no': ('django.db.models.fields.IntegerField', [], {}),
            'cxttype': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CxtLutCxttype']", 'db_column': "u'cxttype'"}),
            'ste_cd': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'appcore.gphtblgph': {
            'Meta': {'object_name': 'GphTblGph', 'db_table': "u'gph_tbl_gph'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'gph_cd': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'gph_no': ('django.db.models.fields.IntegerField', [], {}),
            'ste_cd': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'appcore.plntblpln': {
            'Meta': {'object_name': 'PlnTblPln', 'db_table': "u'pln_tbl_pln'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'pln_cd': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'pln_no': ('django.db.models.fields.IntegerField', [], {}),
            'ste_cd': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'appcore.spftblspf': {
            'Meta': {'object_name': 'SpfTblSpf', 'db_table': "u'spf_tbl_spf'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'spf_cd': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'spf_no': ('django.db.models.fields.IntegerField', [], {}),
            'ste_cd': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        u'appcore.sphtblsph': {
            'Meta': {'object_name': 'SphTblSph', 'db_table': "u'sph_tbl_sph'", 'managed': 'False'},
            'cre_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['appcore.CorTblUsers']"}),
            'cre_on': ('django.db.models.fields.DateTimeField', [], {}),
            'sph_cd': ('django.db.models.fields.CharField', [], {'max_length': '30', 'primary_key': 'True'}),
            'sph_no': ('django.db.models.fields.IntegerField', [], {}),
            'ste_cd': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['appcore']