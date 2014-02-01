__author__ = "Erik Westra"
__license__ = "unknown"
__credits__ = "Francesco de Virgilio"

import os
import os.path
import tempfile
import zipfile

import shutil
import traceback

from osgeo import ogr
from osgeo import osr
from django.contrib.gis.geos.geometry import GEOSGeometry

from .models import Shapefile
from .models import Attribute
from .models import Feature
from .models import AttributeValue
import utils


def import_data(shapefile, character_encoding, description, proj, dateadded):
    # Save the uploaded file into a temporary file on disk.

    fd, fname = tempfile.mkstemp(suffix=".zip")
    os.close(fd)

    f = open(fname, "wb")
    for chunk in shapefile.chunks():
        f.write(chunk)
    f.close()

    # Check that the uploaded file is a zip archive.

    if not zipfile.is_zipfile(fname):
        os.remove(fname)
        return "Not a valid zip archive."

    zip = zipfile.ZipFile(fname)
    # Check that the zip archive contains the required parts of a shapefile.

    required_suffixes = [".shp", ".shx", ".dbf", ".prj"]
    has_suffix = {}
    for suffix in required_suffixes:
        has_suffix[suffix] = False

    for info in zip.infolist():
        extension = os.path.splitext(info.filename)[1].lower()
        if extension in required_suffixes:
            has_suffix[extension] = True

    for suffix in required_suffixes:
        if not has_suffix[suffix]:
            zip.close()
            os.remove(fname)
            return "Archive mising required " + suffix + " file."

    # Extract the contents of the zip archive.

    shapefile_name = None
    dst_dir = tempfile.mkdtemp()
    for info in zip.infolist():
        if info.filename.endswith(".shp"):
            shapefile_name = info.filename

        dst_file = os.path.join(dst_dir, info.filename)
        f = open(dst_file, "wb")
        f.write(zip.read(info.filename))
        f.close()

    zip.close()

    # Open the shapefile.

    try:
        datasource = ogr.Open(os.path.join(dst_dir, shapefile_name))
        layer = datasource.GetLayer(0)
        shapefile_ok = True
    except:
        traceback.print_exc()
        shapefile_ok = False

    if not shapefile_ok:
        os.remove(fname)
        shutil.rmtree(dst_dir)
        return "Not a valid shapefile."

    # Create our Shapefile object to represent the imported shapefile.

    src_spatial_ref = layer.GetSpatialRef()

    geometry_type = layer.GetLayerDefn().GetGeomType()
    geometry_name = utils.ogr_type_to_geometry_name(geometry_type)

    shapefile = Shapefile(filename=shapefile_name,
                          srs_wkt=src_spatial_ref.ExportToWkt(),
                          geom_type=geometry_name,
                          encoding=character_encoding,
                          desc=description,
                          proj=proj,
                          dateadded=dateadded)
    shapefile.save()

    # Store the shapefile's attribute definitions into the database.

    attributes = []
    layer_def = layer.GetLayerDefn()
    for i in range(layer_def.GetFieldCount()):
        field_def = layer_def.GetFieldDefn(i)
        attr = Attribute(shapefile=shapefile,
                         name=field_def.GetName(),
                         type=field_def.GetType(),
                         width=field_def.GetWidth(),
                         precision=field_def.GetPrecision())
        attr.save()
        attributes.append(attr)

    # Set up a coordinate transformation to convert from the shapefile's
    # coordinate system into EPSG 4326 (unprojected lat/long coordinates).

    dst_spatial_ref = osr.SpatialReference()
    dst_spatial_ref.ImportFromEPSG(4326)

    coord_transform = osr.CoordinateTransformation(src_spatial_ref,
                                                   dst_spatial_ref)

    # Process each feature in turn.

    for i in range(layer.GetFeatureCount()):
        src_feature = layer.GetFeature(i)

        # Transform this feature's geometry into EPSG 4326.

        src_geometry = src_feature.GetGeometryRef()
        src_geometry.Transform(coord_transform)
        geometry = GEOSGeometry(src_geometry.ExportToWkt())

        # If necessary, wrap this geometry so that all features have the same
        # geometry type.

        geometry = utils.wrap_geos_geometry(geometry)

        # Calculate the field in the Feature object which will hold the
        # imported feature.

        geometry_field = utils.calc_geometry_field(geometry_name)

        # Create a new Feature object to hold this feature's geometry.

        args = {'shapefile': shapefile, geometry_field: geometry}
        feature = Feature(**args)
        feature.save()

        # Store the feature's attribute values into the database.

        for attr in attributes:
            success, result = utils.get_ogr_feature_attribute(
                attr,
                src_feature,
                character_encoding)
            if not success:
                os.remove(fname)
                shutil.rmtree(dst_dir)
                shapefile.delete()
                return result

            attr_value = AttributeValue(feature=feature,
                                        attribute=attr,
                                        value=result)
            attr_value.save()

    # Finally, clean up.

    os.remove(fname)
    shutil.rmtree(dst_dir)
    return None