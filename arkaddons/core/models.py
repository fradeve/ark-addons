from django.db import models

class ArkProjectModel(models.Model):
    """Stores each ARK project's details and info"""
    projectslug = models.SlugField(max_length=30, blank=False, null=False, verbose_name="Unique project ID")
    projectname = models.CharField(max_length=25, null=True, verbose_name="Project name")
    projectdesc = models.CharField(max_length=150, null=True, verbose_name="Project description")
    arkdbname = models.CharField(max_length=10, null=True, verbose_name="ARK database name")
    arkdbuser = models.CharField(max_length=10, null=True, verbose_name="ARK database user")
    arkdbpassword = models.CharField(max_length=50, null=True, verbose_name="ARK database password")
    arkdbhost = models.CharField(max_length=30, null=True, verbose_name="ARK database host")
    arkdbport = models.SmallIntegerField(max_length=4, blank=True, verbose_name="ARK database port")
    projectstatus = models.BooleanField(default=False)

    @models.permalink
    def get_absolute_url(self):
        return 'ark_project_view', (), {'slug': self.projectslug}