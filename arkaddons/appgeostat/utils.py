from osgeo import ogr
import pyproj

from itertools import izip

from django.contrib.gis.geos import LineString, Point
from django.contrib.gis.geos.collections import MultiPolygon, MultiLineString
from django.contrib.gis.geos.collections import GeometryCollection

__author__ = "Erik Westra"
__credits__ = "Francesco de Virgilio"
__license__ = "unknown"


def ogr_type_to_geometry_name(ogr_type):
    return {ogr.wkbUnknown: "Unknown",
            ogr.wkbPoint: "Point",
            ogr.wkbLineString: "LineString",
            ogr.wkbPolygon: "Polygon",
            ogr.wkbMultiPoint: "MultiPoint",
            ogr.wkbMultiLineString: "MultiLineString",
            ogr.wkbMultiPolygon: "MultiPolygon",
            ogr.wkbGeometryCollection: "GeometryCollection",
            ogr.wkbNone: "None",
            ogr.wkbLinearRing: "LinearRing"}.get(ogr_type)


def wrap_geos_geometry(geometry):
    if geometry.geom_type == "Polygon":
        return MultiPolygon(geometry)
    elif geometry.geom_type == "LineString":
        return MultiLineString(geometry)
    else:
        return geometry


def calc_geometry_field(geometry_type):
    if geometry_type == "Polygon":
        return "geom_multipolygon"
    elif geometry_type == "LineString":
        return "geom_multilinestring"
    else:
        return "geom_" + geometry_type.lower()


def get_ogr_feature_attribute(attr, feature, encoding):
    attr_name = str(attr.name)

    if not feature.IsFieldSet(attr_name):
        return (True, None)

    needs_encoding = False
    if attr.type == ogr.OFTInteger:
        value = str(feature.GetFieldAsInteger(attr_name))
    elif attr.type == ogr.OFTIntegerList:
        value = repr(feature.GetFieldAsIntegerList(attr_name))
    elif attr.type == ogr.OFTReal:
        value = feature.GetFieldAsDouble(attr_name)
        value = "%*.*f" % (attr.width, attr.precision, value)
    elif attr.type == ogr.OFTRealList:
        values = feature.GetFieldAsDoubleList(attr_name)
        str_values = []
        for value in values:
            str_values.append("%*.*f" % (attr.width,
                                         attr.precision,
                                         value))
        value = repr(str_values)
    elif attr.type == ogr.OFTString:
        value = feature.GetFieldAsString(attr_name)
        needs_encoding = True
    elif attr.type == ogr.OFTStringList:
        value = repr(feature.GetFieldAsStringList(attr_name))
        needs_encoding = True
    elif attr.type == ogr.OFTDate:
        parts = feature.GetFieldAsDateTime(attr_name)
        year, month, day, hour, minute, second, tzone = parts
        value = "%d,%d,%d,%d" % (year, month, day, tzone)
    elif attr.type == ogr.OFTTime:
        parts = feature.GetFieldAsDateTime(attr_name)
        year, month, day, hour, minute, second, tzone = parts
        value = "%d,%d,%d,%d" % (hour, minute, second, tzone)
    elif attr.type == ogr.OFTDateTime:
        parts = feature.GetFieldAsDateTime(attr_name)
        year, month, day, hour, minute, second, tzone = parts
        value = "%d,%d,%d,%d,%d,%d,%d" % (year, month,
                day, hour,
                minute, second, tzone)
    else:
        return (False, "Unsupported attribute type: " +
                       str(attr.type))

    if needs_encoding:
        try:
            value = value.decode(encoding)
        except UnicodeDecodeError:
            return (False, "Unable to decode value in " +
                    repr(attr_name) + " attribute.&nbsp; " +
                    "Are you sure you're using the right " +
                    "character encoding?")

    return (True, value)


def unwrap_geos_geometry(geometry):
    if geometry.geom_type in ["MultiPolygon",
                              "MultiLineString"]:
        if len(geometry) == 1:
            geometry = geometry[0]

    return geometry


def set_ogr_feature_attribute(attr, value, feature, encoding):
    attr_name = str(attr.name)

    if value is None:
        feature.UnsetField(attr_name)
        return

    if attr.type == ogr.OFTInteger:
        feature.SetField(attr_name, int(value))
    elif attr.type == ogr.OFTIntegerList:
        integers = eval(value)
        feature.SetFieldIntegerList(attr_name, integers)
    elif attr.type == ogr.OFTReal:
        feature.SetField(attr_name, float(value))
    elif attr.type == ogr.OFTRealList:
        floats = []
        for s in eval(value):
            floats.append(eval(s))
        feature.SetFieldDoubleList(attr_name, floats)
    elif attr.type == ogr.OFTString:
        feature.SetField(attr_name, value.encode(encoding))
    elif attr.type == ogr.OFTStringList:
        strings = []
        for s in eval(value):
            strings.append(s.encode(encoding))
        feature.SetFieldStringList(attr_name, strings)
    elif attr.type == ogr.OFTDate:
        parts = value.split(",")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        tzone = int(parts[3])
        feature.SetField(attr_name, year, month, day,
                         0, 0, 0, tzone)
    elif attr.type == ogr.OFTTime:
        parts = value.split(",")
        hour = int(parts[0])
        minute = int(parts[1])
        second = int(parts[2])
        tzone = int(parts[3])
        feature.SetField(attr_name, 0, 0, 0,
                         hour, minute, second, tzone)
    elif attr.type == ogr.OFTDateTime:
        parts = value.split(",")
        year = int(parts[0])
        month = int(parts[1])
        day = int(parts[2])
        hour = int(parts[3])
        minute = int(parts[4])
        second = int(parts[5])
        tzone = int(parts[6])
        feature.SetField(attr_name, year, month, day,
                         hour, minute, second, tzone)


def calc_search_radius(latitude, longitude, distance):
    geod = pyproj.Geod(ellps="WGS84")

    x, y, angle = geod.fwd(longitude, latitude, 0, distance)
    radius = y-latitude

    x, y, angle = geod.fwd(longitude, latitude, 90, distance)
    radius = max(radius, x-longitude)

    x, y, angle = geod.fwd(longitude, latitude, 180, distance)
    radius = max(radius, latitude-y)

    x, y, angle = geod.fwd(longitude, latitude, 270, distance)
    radius = max(radius, longitude-x)

    return radius


def get_geos_geometry(shp):
    feat_list = []
    geom_field = calc_geometry_field(shp.geom_type)
    for feature in shp.feature_set.all():
        geometry = getattr(feature, geom_field)
        geometry = unwrap_geos_geometry(geometry)
        feat_list.append(geometry)
    geometry = GeometryCollection(feat_list)
    return geometry


def grouped(iterable, n):
    return izip(*[iter(iterable)]*n)


def get_side_dict(polygon, custom_srid):
    side_dict = {}
    points_list = polygon.poly.coords[0]
    for i, point in enumerate(points_list):
        new_side_line = LineString(point, points_list[i-1], srid=custom_srid)
        new_side_len = new_side_line.length
        new_side = {new_side_line: new_side_len}
        side_dict.update(new_side)
    return side_dict
