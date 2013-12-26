Core
----
Contains the API tool: allows to create a set of APIs from any ARK project.
Simply activate the app, go to the main page, create a new project inserting
all the details and parameters to connect to the MySQL ARK's database.

A set of APIs will be generated at
``http://somewebsite.com/api/<arkproject_id>/all``; the default API is in JSON format,
while XML could be obtained appending ``?format=xml``.

The fundamental block of this API is the "archaeological context" or
"stratigraphic unit". Every attribute extracted from the database is attached
to the corresponding context, and stored in one of its fields. The following
main fields have been defined:

*cre_on*
    creation date
*cxttype*
    the context type
*cre_by*
    the ARK user who created the context
*frag_txt*
    all the attributes containing just text
*frag_attrs*
    all the attributes consisting of pre-defined values
*frag_date*
    all the attributes consisting of dates
*frag_geo*
    the content of the SHP file eventually attached to the context, rendered as geoJSON
*cxt_cd*
    the unique context code
*cxt_no*
    the unique context number
*ste_cd*
    the site code for the project in which the current context is contained

With this in mind, other useful URLs are:

``http://somewebsite.com/<arkproject_id>/<context_code>``
    gets just a context

``http://somewebsite.com/<arkproject_id>/<context_code>?<frag_type>=<attr>``
    gets the ``<attr>`` from the ``<frag_type>`` for the context

Note on geo components
^^^^^^^^^^^^^^^^^^^^^^

* At the moment, a link to the WFS for the current project must be defined to get
  all the geo-related information for the contexts.
* The name of the WFS layer from which geometries must be taken is hardcoded in
  the serializer method; this will be fixed in the future.

At the moment, all the context's information is stored in the ARK database, and
the corresponding SHP files stores only the context's geometries. Following this
convention, even if the SHP file's table will have attributes, they will not be
exported in the geoJSON (which will contain, instead, all the information about
the current layer).

Note on the database mapping
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Django creates an abstraction layer of ARK's MySQL database; it's defined in
``arkaddons/appcore/arkmodels.py``. Only the tables containing actual archaeological
data useful to reconstruct the context structure have been mapped, leaving apart
all those tables related to the characteristics of the PHP application.

Models have been derived from the MySQL database provided with ARK v. 1.0.
