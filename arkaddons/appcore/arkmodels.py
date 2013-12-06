from __future__ import unicode_literals

__appname__ = "appcore"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from django.db import models


class CorTblUsers(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    initials = models.CharField(unique=True, max_length=10, blank=True)
    sfilter = models.IntegerField()
    email = models.CharField(max_length=100, blank=True)
    account_enabled = models.IntegerField()
    cre_by = models.IntegerField()
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_users'

class CorLutAttributetype(models.Model):
    id = models.IntegerField(primary_key=True)
    attributetype = models.CharField(max_length=255)
    module = models.CharField(max_length=3)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_attributetype'


class AbkLutAbktype(models.Model):
    id = models.IntegerField(primary_key=True)
    abktype = models.CharField(max_length=50)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'abk_lut_abktype'


class AbkTblAbk(models.Model):
    abk_cd = models.CharField(primary_key=True, max_length=30)
    abk_no = models.IntegerField()
    ste_cd = models.CharField(max_length=10)
    abktype = models.ForeignKey(AbkLutAbktype, db_column='abktype')                 # linked
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'abk_tbl_abk'


class AelTblAel(models.Model):
    ael_cd = models.CharField(primary_key=True, max_length=30)
    ael_no = models.IntegerField()
    ste_cd = models.CharField(max_length=10)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ael_tbl_ael'


class CnsTblCns(models.Model):
    cns_cd = models.CharField(primary_key=True, max_length=30)
    cns_no = models.IntegerField()
    ste_cd = models.CharField(max_length=10)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cns_tbl_cns'


class CorLutActiontype(models.Model):
    id = models.IntegerField(primary_key=True)
    actiontype = models.CharField(max_length=255)
    module = models.CharField(max_length=3)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_actiontype'


class CorLutAliastype(models.Model):
    id = models.IntegerField(primary_key=True)
    aliastype = models.CharField(max_length=50)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_aliastype'


class CorLutAttribute(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.CharField(max_length=255)
    attributetype = models.ForeignKey(CorLutAttributetype, db_column='attributetype')   # linked
    module = models.CharField(max_length=3)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                         # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_attribute'


class CorLutDatetype(models.Model):
    id = models.IntegerField(primary_key=True)
    datetype = models.CharField(max_length=255)
    module = models.CharField(max_length=3)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_datetype'


class CorLutFiletype(models.Model):
    id = models.IntegerField(primary_key=True)
    filetype = models.CharField(max_length=50)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_filetype'


class CorLutFile(models.Model):
    id = models.IntegerField(primary_key=True)
    filename = models.CharField(max_length=255)
    uri = models.TextField(blank=True)
    filetype = models.ForeignKey(CorLutFiletype, db_column='filetype')  # linked
    module = models.CharField(max_length=255)
    batch = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')         # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_file'


class CorLutLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=10)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')         # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_language'


class CorLutNumbertype(models.Model):
    id = models.IntegerField(primary_key=True)
    numbertype = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    qualifier = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')         # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_numbertype'


class CorLutSpantype(models.Model):
    id = models.IntegerField(primary_key=True)
    spantype = models.CharField(max_length=255)
    meta = models.TextField()
    evaluation = models.TextField()
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')         # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_spantype'


class CorLutSpanlabel(models.Model):
    id = models.IntegerField(primary_key=True)
    spantype = models.ForeignKey(CorLutSpantype, db_column='spantype')  # linked
    typemod = models.CharField(max_length=3)
    spanlabel = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')         # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_spanlabel'


class CorLutTxttype(models.Model):
    id = models.IntegerField(primary_key=True)
    txttype = models.CharField(max_length=255)
    module = models.CharField(max_length=3)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')         # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_lut_txttype'

    def __unicode__(self):
        return '%s' % self.txttype


###### START IGNORED MODELS
# These models are related to the ARK Php interface more then data,
# so have been ignored


class CorLvuApplications(models.Model):
    application_id = models.IntegerField(unique=True, blank=True, null=True)
    application_define_name = models.CharField(unique=True, max_length=32, blank=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_applications'


class CorLvuApplicationsSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_applications_seq'


class CorLvuAreaAdminAreas(models.Model):
    area_id = models.IntegerField(blank=True, null=True)
    perm_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_area_admin_areas'


class CorLvuAreas(models.Model):
    area_id = models.IntegerField(unique=True, blank=True, null=True)
    application_id = models.IntegerField(blank=True, null=True)
    area_define_name = models.CharField(max_length=32, blank=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_areas'


class CorLvuAreasSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_areas_seq'


class CorLvuGroupSubgroups(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    subgroup_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_group_subgroups'


class CorLvuGrouprights(models.Model):
    group_id = models.IntegerField(blank=True, null=True)
    right_id = models.IntegerField(blank=True, null=True)
    right_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_grouprights'


class CorLvuGroups(models.Model):
    group_id = models.IntegerField(unique=True, blank=True, null=True)
    group_type = models.IntegerField(blank=True, null=True)
    group_define_name = models.CharField(unique=True, max_length=32, blank=True)
    is_active = models.IntegerField(blank=True, null=True)
    owner_user_id = models.IntegerField(blank=True, null=True)
    owner_group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_groups'


class CorLvuGroupsSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_groups_seq'


class CorLvuGroupusers(models.Model):
    perm_user_id = models.IntegerField(blank=True, null=True)
    group_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_groupusers'


class CorLvuPermUsers(models.Model):
    perm_user_id = models.IntegerField(unique=True, blank=True, null=True)
    auth_user_id = models.CharField(max_length=32, blank=True)
    auth_container_name = models.CharField(max_length=32, blank=True)
    perm_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_perm_users'


class CorLvuPermUsersSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_perm_users_seq'


class CorLvuRightImplied(models.Model):
    right_id = models.IntegerField(blank=True, null=True)
    implied_right_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_right_implied'


class CorLvuRights(models.Model):
    right_id = models.IntegerField(unique=True, blank=True, null=True)
    area_id = models.IntegerField(blank=True, null=True)
    right_define_name = models.CharField(max_length=32, blank=True)
    has_implied = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_rights'


class CorLvuRightsSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_rights_seq'


class CorLvuTranslations(models.Model):
    translation_id = models.IntegerField(unique=True, blank=True, null=True)
    section_id = models.IntegerField(blank=True, null=True)
    section_type = models.IntegerField(blank=True, null=True)
    language_id = models.CharField(max_length=32, blank=True)
    name = models.CharField(max_length=32, blank=True)
    description = models.CharField(max_length=32, blank=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_translations'


class CorLvuTranslationsSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_translations_seq'


class CorLvuUserrights(models.Model):
    perm_user_id = models.IntegerField(blank=True, null=True)
    right_id = models.IntegerField(blank=True, null=True)
    right_level = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_userrights'


class CorLvuUsers(models.Model):
    auth_user_id = models.CharField(unique=True, max_length=32, blank=True)
    handle = models.CharField(max_length=32, blank=True)
    passwd = models.CharField(max_length=32, blank=True)
    owner_user_id = models.IntegerField(blank=True, null=True)
    owner_group_id = models.IntegerField(blank=True, null=True)
    lastlogin = models.DateTimeField(blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_users'


class CorLvuUsersSeq(models.Model):
    sequence = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'cor_lvu_users_seq'

###### END IGNORED MODELS


class CorTblAlias(models.Model):
    id = models.IntegerField(primary_key=True)
    alias = models.CharField(max_length=255)
    aliastype = models.ForeignKey(CorLutAliastype, db_column='aliastype')       # linked
    language = models.CharField(max_length=10)
    itemkey = models.CharField(max_length=50)                   # FIXME
    itemvalue = models.CharField(max_length=50)                 # FIXME
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                 # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_alias'


class CorTblCmap(models.Model):                                 # ignored
    id = models.IntegerField(primary_key=True)
    nname = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    sourcedb = models.CharField(max_length=15)
    stecd = models.CharField(max_length=50)
    import_cre_by = models.IntegerField()
    import_cre_on = models.DateTimeField()
    type = models.CharField(max_length=50)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_cmap'


class CorTblCmapData(models.Model):                             # ignored
    id = models.IntegerField(primary_key=True)
    cmap = models.CharField(max_length=100)
    sourcedata = models.CharField(max_length=255)
    sourcelocation = models.CharField(max_length=255)
    mapto_tbl = models.CharField(max_length=255)
    mapto_id = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    cre_by = models.CharField(max_length=15)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_cmap_data'


class CorTblCmapStructure(models.Model):                        # ignored
    id = models.IntegerField(primary_key=True)
    cmap = models.IntegerField()
    tbl = models.CharField(max_length=255)
    col = models.CharField(max_length=255)
    class_field = models.CharField(db_column='class', max_length=50)  # Field renamed because it was a Python reserved word.
    uid_col = models.CharField(max_length=255)
    itemkey = models.CharField(max_length=50)
    raw_itemval_tbl = models.CharField(max_length=255)
    raw_itemval_col = models.CharField(max_length=255)
    raw_itemval_join_col = models.CharField(max_length=255)
    raw_stecd_col = models.CharField(max_length=255)
    raw_stecd_join_col = models.CharField(max_length=255)
    raw_stecd_tbl = models.CharField(max_length=255)
    tbl_itemval_join_col = models.CharField(max_length=255)
    tbl_stecd_join_col = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    lang = models.CharField(max_length=50)
    true = models.CharField(max_length=255)
    false = models.CharField(max_length=255)
    notset = models.CharField(max_length=255)
    lut_tbl = models.CharField(max_length=255)
    lut_idcol = models.CharField(max_length=255)
    lut_valcol = models.CharField(max_length=255)
    end_source_col = models.CharField(max_length=255)
    xmi_itemkey = models.CharField(max_length=10)
    xmi_itemval_col = models.CharField(max_length=100)
    ark_mod = models.CharField(max_length=3)
    log = models.CharField(max_length=3)

    class Meta:
        managed = False
        db_table = 'cor_tbl_cmap_structure'


class CorTblCol(models.Model):                              # ignored
    id = models.IntegerField(primary_key=True)
    dbname = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_col'


class CorTblFile(models.Model):                             # ignored
    id = models.IntegerField(primary_key=True)
    itemkey = models.CharField(max_length=50)
    itemvalue = models.CharField(max_length=30)
    file = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_file'


class CorTblFilter(models.Model):                           # ignored
    id = models.IntegerField(primary_key=True)
    filter = models.TextField()
    type = models.CharField(max_length=6)
    nname = models.CharField(max_length=255)
    sgrp = models.IntegerField()
    cre_by = models.CharField(max_length=3)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_filter'


class CorTblLog(models.Model):                              # ignored
    id = models.IntegerField(primary_key=True)
    event = models.CharField(max_length=10)
    ref = models.CharField(max_length=255)
    refid = models.CharField(max_length=255)
    vars = models.TextField()
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_log'


class CorTblMarkup(models.Model):                           # ignored
    id = models.IntegerField(primary_key=True)
    nname = models.CharField(max_length=25)
    markup = models.TextField()
    mod_short = models.TextField()
    language = models.CharField(max_length=10)
    description = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_markup'


class CorTblModule(models.Model):                           # ignored
    id = models.IntegerField(primary_key=True)
    itemkey = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    shortform = models.CharField(max_length=3)
    description = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_module'


class CorTblNumber(models.Model):
    id = models.IntegerField(primary_key=True)
    numbertype = models.ForeignKey(CorLutNumbertype, db_column='numbertype')        # linked
    typemod = models.CharField(max_length=3)
    itemkey = models.CharField(max_length=255)
    itemvalue = models.CharField(max_length=30)
    fragtype = models.CharField(max_length=10)
    fragid = models.IntegerField()
    number = models.FloatField()
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_number'


class CorTblSgrp(models.Model):                             # ignored
    id = models.IntegerField(primary_key=True)
    sgrp = models.CharField(max_length=100)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_sgrp'


class CorTblSpan(models.Model):
    id = models.IntegerField(primary_key=True)
    spantype = models.ForeignKey(CorLutSpantype, db_column='spantype')              # linked
    typemod = models.CharField(max_length=3)
    itemkey = models.CharField(max_length=10)
    itemvalue = models.CharField(max_length=30)
    beg = models.CharField(max_length=255)
    end = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_span'


class CorTblSpanattr(models.Model):
    id = models.IntegerField(primary_key=True)
    span = models.IntegerField()
    spanlabel = models.ForeignKey(CorLutSpanlabel, db_column='spanlabel')           # linked
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_spanattr'


class CorTblSte(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    description = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_ste'


class CxtLutCxttype(models.Model):
    id = models.IntegerField(primary_key=True)
    cxttype = models.CharField(max_length=255)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cxt_lut_cxttype'

    def __unicode__(self):
        return '%s' % self.cxttype


class CxtTblCxt(models.Model):
    cxt_cd = models.CharField(primary_key=True, max_length=30)
    cxt_no = models.IntegerField()
    ste_cd = models.CharField(max_length=10)
    cxttype = models.ForeignKey(CxtLutCxttype, db_column='cxttype')                 # linked
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cxt_tbl_cxt'


class CorTblTxt(models.Model):
    id = models.IntegerField(primary_key=True)
    txttype = models.ForeignKey(CorLutTxttype, db_column='txttype')                 # linked
    itemkey = models.CharField(max_length=50)
    itemvalue = models.ForeignKey(CxtTblCxt, db_column='itemvalue', related_name='frag_txt')                 # linked
    txt = models.TextField()
    language = models.CharField(max_length=10)
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                     # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_txt'

    def __unicode__(self):
        return '%s' % self.txt


class CorTblAttribute(models.Model):
    id = models.IntegerField(primary_key=True)
    attribute = models.ForeignKey(CorLutAttribute, db_column='attribute')
    itemkey = models.CharField(max_length=50)
    itemvalue = models.ForeignKey(CxtTblCxt, db_column='itemvalue', related_name='frag_attrs')      # linked
    boolean = models.IntegerField()
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                 # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_attribute'


class CorTblDate(models.Model):
    id = models.IntegerField(primary_key=True)
    datetype = models.ForeignKey(CorLutDatetype, db_column='datetype')          # linked
    itemkey = models.CharField(max_length=50)
    itemvalue = models.ForeignKey(CxtTblCxt, db_column='itemvalue', related_name='frag_date')   # linked
    datefield = models.DateTimeField(db_column='date')
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                 # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_date'


class CorTblAction(models.Model):
    id = models.IntegerField(primary_key=True)
    actiontype = models.ForeignKey(CorLutActiontype, db_column='actiontype')    # linked
    itemkey = models.CharField(max_length=50)
    itemvalue = models.ForeignKey(CxtTblCxt, db_column='itemvalue')             # linked
    actor_itemkey = models.CharField(max_length=50)
    actor_itemvalue = models.ForeignKey(AbkTblAbk, db_column='actor_itemvalue') # linked
    cre_by = models.ForeignKey(CorTblUsers, db_column='cre_by')                 # linked
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_action'


class CorTblWmc(models.Model):                              # ignored
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    comments = models.CharField(max_length=255)
    wmc = models.TextField()
    scales = models.TextField()
    extents = models.TextField()
    projection = models.CharField(max_length=255)
    zoom = models.IntegerField()
    legend_array = models.TextField()
    osm = models.IntegerField(db_column='OSM') # Field name made lowercase.
    gmap_api_key = models.CharField(max_length=255)
    public = models.IntegerField()
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_wmc'


class CorTblWwwpages(models.Model):                         # ignored
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sortposs = models.IntegerField()
    file = models.CharField(max_length=255)
    sgrp = models.CharField(max_length=255)
    navname = models.CharField(max_length=255)
    navlinkvars = models.CharField(max_length=255)
    defaultvars = models.TextField()
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_wwwpages'


class CorTblXmi(models.Model):                              # ignored
    id = models.IntegerField(primary_key=True)
    itemkey = models.CharField(max_length=20)
    itemvalue = models.CharField(max_length=20)
    xmi_itemkey = models.CharField(max_length=20)
    xmi_itemvalue = models.CharField(max_length=20)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cor_tbl_xmi'


class GphTblGph(models.Model):                          # ignored
    gph_cd = models.CharField(primary_key=True, max_length=30)
    gph_no = models.IntegerField()
    ste_cd = models.CharField(max_length=10)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'gph_tbl_gph'


class PlnTblPln(models.Model):                          # ignored
    pln_cd = models.CharField(primary_key=True, max_length=30)
    pln_no = models.IntegerField()
    ste_cd = models.CharField(max_length=10)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'pln_tbl_pln'


class SpfTblSpf(models.Model):                          # ignored
    spf_cd = models.CharField(primary_key=True, max_length=30)
    spf_no = models.IntegerField()
    ste_cd = models.CharField(max_length=10)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'spf_tbl_spf'


class SphTblSph(models.Model):                          # ignored
    sph_cd = models.CharField(primary_key=True, max_length=30)
    sph_no = models.IntegerField()
    ste_cd = models.CharField(max_length=10)
    cre_by = models.ForeignKey(CorTblUsers)
    cre_on = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sph_tbl_sph'