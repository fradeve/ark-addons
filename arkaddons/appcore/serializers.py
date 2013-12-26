__appname__ = "arkaddons.appcore"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

import django.conf as conf

from rest_framework import serializers
from rest_framework.relations import RelatedField

from osgeo import ogr
import json

from .arkmodels import CxtTblCxt, CxtLutCxttype, CorTblUsers, CorTblTxt,\
    CorTblAttribute, CorLutAttribute, CorLutAttributetype, CorTblDate,\
    CorLutDatetype


### Type 0: the context
class CxttypeSerializer(serializers.ModelSerializer):
    """Returns CxtLutCxttype serialized data"""

    class Meta:
        model = CxtLutCxttype
        fields = ('cxttype',)


### Type 0: the user
class CorTblUsersSerializer(serializers.ModelSerializer):
    """Returns CorTblUsers serialized data"""

    class Meta:
        model = CorTblUsers
        fields = ('firstname', 'lastname')


### Type 1: text fragments
class FragTxtSerializer(serializers.ModelSerializer):
    """Returns CorTblTxt serialized data"""
    txttype = RelatedField()

    class Meta:
        model = CorTblTxt
        fields = ('txttype', 'txt')


### Type 2: attributes
class AttrsLutTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = CorLutAttributetype
        fields = ('attributetype', 'module')


class AttrsLutSerializer(serializers.ModelSerializer):
    attributetype = AttrsLutTypeSerializer()

    class Meta:
        model = CorLutAttribute
        fields = ('attribute', 'attributetype')


class FragAttrsSerializer(serializers.ModelSerializer):
    attribute = AttrsLutSerializer()

    class Meta:
        model = CorTblAttribute
        fields = ('attribute', 'boolean', 'cre_on')


### Type 3: events
class FragDatetypeSerializer(serializers.Serializer):
    datetype = RelatedField()

    class Meta:
        model = CorLutDatetype
        fields = ('datetype',)


class FragEventsSerializer(serializers.Serializer):
    datetype = FragDatetypeSerializer()
    datefield = serializers.DateTimeField()

    class Meta:
        model = CorTblDate
        fields = ('datetype', 'datefield')


### The main serializer class
class CxtSerializer(serializers.ModelSerializer):
    """Returns serializer"""
    cre_on = serializers.DateTimeField()
    cxttype = CxttypeSerializer()
    cre_by = CorTblUsersSerializer()
    frag_txt = FragTxtSerializer()
    frag_attrs = FragAttrsSerializer()
    #frag_spans
    frag_date = FragEventsSerializer()  # need to link action to event
    frag_geo = serializers.SerializerMethodField('get_geo')

    class Meta:
        model = CxtTblCxt

    def get_geo(self, obj):
        """
        Get the current context and returns
        all the associated shapefiles as geoJSON.
        """

        # scans available DB for the current project and takes the WFS value
        for setting in conf.settings.DATABASES:
            # get the current project settings
            if obj.ste_cd in conf.settings.DATABASES[setting].values():
                # WFS field in db is null=True
                if conf.settings.DATABASES[setting]['WFS'] is None:
                    return "None"
                else:
                    # retrieves the layer from the SHP
                    # and filters it using current context id
                    driver = ogr.GetDriverByName('WFS')
                    wfs = driver.Open(
                        'WFS:' + conf.settings.DATABASES[setting]['WFS'])
                    layer = wfs.GetLayerByName('cxt_schm')  # FIXME
                    query = "ark_id = '" + obj.ste_cd + \
                            '_' + str(obj.cxt_no) + "'"
                    layer.SetAttributeFilter(str(query))
                    # creates a new dictionary on which append the geoJSON
                    features = {}
                    # export geometry as geoJSON,
                    # transform in dict and append to main dict
                    for feature in layer:
                        selectedfeat = json.loads(feature.ExportToJson())
                        features.update(selectedfeat)
                    return features
            else:
                pass
