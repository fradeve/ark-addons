__appname__ = "appgeostat"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = "0.1"

from django import forms

CHARACTER_ENCODINGS = [
    ("ascii", "ASCII"),
    ("latin1", "Latin-1"),
    ("utf8", "UTF-8")]


class ImportShapefileForm(forms.Form):
    import_file = forms.FileField(label="Select a zipped Shapefile")
    character_encoding = forms.ChoiceField(choices=CHARACTER_ENCODINGS,
                                           initial="utf8")
    description = forms.CharField(label="Description for this file")
    projection = forms.IntegerField(label="Cartographic projection")
