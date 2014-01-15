from django.contrib.gis.db import models
from django.db.models import Sum, Avg


class Shapefile(models.Model):
    filename = models.CharField(max_length=255, null=True)
    srs_wkt = models.CharField(max_length=255, null=True)
    geom_type = models.CharField(max_length=50, null=True)
    encoding = models.CharField(max_length=20, null=True)
    desc = models.CharField(max_length=500, null=True)
    dateadded = models.DateTimeField(null=True)
    classes = models.IntegerField(null=True)
    jnb = models.CharField(max_length=500, null=True)

    def __unicode__(self):
        return self.filename

    @models.permalink
    def get_absolute_url(self):
        return 'shape_detail', (), {'pk': self.id}

    def count_features(self):
        return self.feature_set.count()

    def ditches_count(self):
        return self.helperditchesnumber_set.filter(type='ditch').count()

    def ditches_perimeter(self):
        try:
            return int(self.helperditchesnumber_set.filter(type='ditch')
                       .aggregate(Sum('perimeter'))['perimeter__sum'])/2
        except:
            return None

    def ditches_area(self):
        try:
            return self.helpercompoundsarea_set.filter(type='ditch')\
                .aggregate(Sum('storedarea'))['storedarea__sum']
        except:
            return None

    def ditches_avg_area(self):
        try:
            return self.helpercompoundsarea_set.filter(type='ditch') \
                .aggregate(Avg('storedarea'))['storedarea__avg']
        except:
            return None

    def compounds_count(self):
        try:
            return self.helperditchesnumber_set.filter(type='compound').count()
        except:
            return None

    def compounds_perimeter(self):
        try:
            return int(self.helperditchesnumber_set.filter(type='compound')
                       .aggregate(Sum('perimeter'))['perimeter__sum'])/2
        except:
            return None

    def compounds_area(self):
        try:
            return self.helpercompoundsarea_set.filter(type='compound') \
                .aggregate(Sum('storedarea'))['storedarea__sum']
        except:
            return None

    def compounds_avg_area(self):
        try:
            return self.helpercompoundsarea_set.filter(type='compound') \
                .aggregate(Avg('storedarea'))['storedarea__avg']
        except:
            return None


class Attribute(models.Model):
    shapefile = models.ForeignKey(Shapefile)
    name = models.CharField(max_length=255, null=True)
    type = models.IntegerField()
    width = models.IntegerField()
    precision = models.IntegerField()

    def __unicode__(self):
        return self.filename


class Feature(models.Model):
    """
    The inability of Shapefiles to distinguish between Polygons and
    MultiPolygons forces us to store all the Polygons as MultiPolygons and
    all LineString as MultiLineString.
    Use the functions in utils.py to 'wrap' and 'unwrap' geometries in the
    correct formats.
    """
    shapefile = models.ForeignKey(Shapefile)
    geom_point = \
        models.PointField(srid=4326,
                          blank=True, null=True)
    geom_multipoint = \
        models.MultiPointField(srid=4326,
                               blank=True, null=True)
    geom_multilinestring = \
        models.MultiLineStringField(srid=4326,
                                    blank=True, null=True)
    geom_multipolygon = \
        models.MultiPolygonField(srid=4326,
                                 blank=True, null=True)
    geom_geometrycollection = \
        models.GeometryCollectionField(srid=4326,
                                       blank=True,
                                       null=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return unicode(self.id) or u''


class AttributeValue(models.Model):
    feature = models.ForeignKey(Feature)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=255,
                             blank=True, null=True)

    def __unicode__(self):
        return unicode(self.value)


class HelperSettlementArea(models.Model):
    """
    Table to save all the helper layer containing settlements area
    """
    shapefile = models.ForeignKey(Shapefile)
    objects = models.GeoManager()
    poly = models.PolygonField()
    storedarea = models.FloatField(null=True)


class HelperDitchesNumber(models.Model):
    """
    Table to save the helper layer containing data about ditches and compounds
    """
    shapefile = models.ForeignKey(Shapefile)
    objects = models.GeoManager()
    poly = models.MultiPolygonField(srid=3857)
    perimeter = models.FloatField(null=True)
    class_n = models.IntegerField(null=True)
    type = models.TextField(max_length=255, null=True)


class HelperCompoundsArea(models.Model):
    """
    Table to save all the helper layer containing compounds area
    """
    shapefile = models.ForeignKey(Shapefile)
    objects = models.GeoManager()
    poly = models.PolygonField(srid=3857)
    storedarea = models.FloatField(null=True)
    type = models.TextField(max_length=255, null=True)
