__appname__ = "appgeostat"
__author__ = "Francesco de Virgilio (fradeve)"
__license__ = "GNU GPL 3.0 or later"

__version__ = "0.1"

from math import sin, cos, radians

from django.contrib.gis.geos import Point


def get_round_vertex(angle, radius, point_x, point_y, projection=3857, rotation=0):
    """
    Returns a list of GEOS points representing a circle around the point
    (point_x, point_y) of radius `radius`, separated of an `angle` value (in
    degrees) from the next point.
    :param angle:
    :param radius:
    :param point_x:
    :param point_y:
    :return:
    """
    vertex_list = []
    angle_orig = angle
    while angle <= 360:
        vertex_x = point_x + radius * cos(radians(angle))
        vertex_y = point_y + radius * sin(radians(angle))
        if rotation > 0:
            x = ((vertex_x - point_x)*cos(rotation) - (vertex_y - point_y)
                 * sin(rotation)) + point_x
            y = ((vertex_x - point_x)*sin(rotation) + (vertex_y - point_y)
                 * cos(rotation)) + point_y
            vertex_list.append(Point(x, y, srid=projection))
        else:
            vertex_list.append(Point(vertex_x, vertex_y, srid=projection))
        angle += angle_orig

    return vertex_list


def check_nearest_point(coords_tuple, srid, refer_pt, defined_nearest):
    """
    Checks if the point generated by a tuple of coordinates (x, y) of reference
    system ID `srid` is near to a reference point `refer_pt` more of an already
    defined value `defined_nearest`; if true, updates the `refer_pt` list with
    the nearest GEOS Point `refer_pt[0]` and the distance `refer_pt[1]`.
    :param coords_tuple:
    :param srid:
    :param refer_pt:
    :param defined_nearest:
    :return:
    """
    cur_point = Point(coords_tuple, srid=srid)
    if cur_point.distance(refer_pt) < defined_nearest[1]:
        defined_nearest = [cur_point, cur_point.distance(refer_pt)]
    else:
        pass
    return defined_nearest