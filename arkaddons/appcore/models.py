from django.db import models
from django.db.models import signals
import django.conf as conf


class ArkProjectModel(models.Model):
    """Stores each ARK project's details and info"""
    projectslug = models.SlugField(
        max_length=30,
        blank=False,
        null=False,
        verbose_name="Unique project ID")
    projectname = models.CharField(
        max_length=25,
        null=True,
        verbose_name="Project name")
    projectdesc = models.CharField(
        max_length=150,
        null=True,
        verbose_name="Project description")
    projectsitecode = models.CharField(
        max_length=10,
        blank=False,
        verbose_name="Site code for this project")
    arkdbname = models.CharField(
        max_length=20,
        null=True,
        verbose_name="ARK database name")
    arkdbuser = models.CharField(
        max_length=10,
        null=True,
        verbose_name="ARK database user")
    arkdbpassword = models.CharField(
        max_length=50,
        null=True,
        verbose_name="ARK database password")
    arkdbhost = models.CharField(
        max_length=30,
        null=True,
        verbose_name="ARK database host")
    arkdbport = models.SmallIntegerField(
        max_length=4,
        blank=True,
        verbose_name="ARK database port")
    arkwfsaddress = models.URLField(
        null=True,
        blank=True,
        verbose_name="ARK WFS link")

    @models.permalink
    def get_absolute_url(self):
        return 'ark_detail_view', (), {'slug': self.projectslug}


def addappdb(sender, instance, created, **kwargs):
    """Add database to the conf.settings.DATABASES dict just
    after creation, using the post_save signal"""
    if created:
        arkappdbname = 'ark_' + instance.projectslug.encode('utf8')
        conf.settings.DATABASES[arkappdbname] = {
            'ENGINE': 'django.db.backends.mysql',
            'AUTOCOMMIT': True,
            'ATOMIC_REQUESTS': False,
            'NAME': instance.arkdbname.encode('utf8'),
            'TEST_MIRROR': None,
            'CONN_MAX_AGE': 0,
            'TEST_NAME': None,
            'TIME_ZONE': 'UTC',
            'TEST_COLLATION': None,
            'OPTIONS': {},
            'HOST': instance.arkdbhost.encode('utf8'),
            'USER': instance.arkdbuser.encode('utf8'),
            'TEST_CHARSET': None,
            'PASSWORD': instance.arkdbpassword.encode('utf8'),
            'PORT': instance.arkdbport,
            'WFS': instance.arkwfsaddress,
            'STECD': instance.projectsitecode.encode('utf8')}

signals.post_save.connect(addappdb, sender=ArkProjectModel)