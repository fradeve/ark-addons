__appname__ = "stats"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from django import forms

from .models import StatsProjectModel, StatsMapModel, ApiFieldsModel

class ApiFieldsForm(forms.ModelForm):
    class Meta:
        model = ApiFieldsModel
        exclude = ('map', 'cxt')


class StatsCreateForm(forms.ModelForm):

    class Meta:
        model = StatsProjectModel
        exclude = ('map',)
