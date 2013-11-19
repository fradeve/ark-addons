__appname__ = "arkaddons.core"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = ""

from rest_framework import serializers
from rest_framework.relations import RelatedField
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
    #frag_geo

    class Meta:
        model = CxtTblCxt