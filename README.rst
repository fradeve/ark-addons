==========
ARK Addons
==========

This project is a Django web interface to obtain statistical information from
an [ARK](http://ark.lparchaeology.com) (Archaeological Recording Kit) project.
It is aimed to mine data from archaeological databases and create customizable
visualizations, querying both text and geographical data.
It consists of separate tools, each one is a Django app; they could be activated
independently (although it could be useful activate them all together).

Core
----
Contains the API tool: allows to create a set of APIs from any ARK project.
Simply activate the app, go to the main page, create a new project inserting
all the details and parameters to connect to the MySQL ARK's database.

A set of APIs will be generated at
`http://somewebsite.com/api/<arkproject_id>/all`; the default API is in JSON format,
while XML could be obtained appending `?format=xml`.

The fundamental block of this API is the "archaeological context" or
"stratigraphic unit". Every attribute extracted from the database is attached
to the corresponding context, and stored in one of its fields. The following
main fields have been defined:

cre_on
    creation date
cxttype
    the context type
cre_by
    the ARK user who created the context
frag_txt
    all the attributes containing just text
frag_attrs
    all the attributes consisting of pre-defined values
frag_date
    all the attributes consisting of dates
frag_geo
    the content of the SHP file eventually attached to the context, rendered as geoJSON
cxt_cd
    the unique context code
cxt_no
    the unique context number
ste_cd
    the site code for the project in which the current context is contained

With this in mind, other useful URLs are:

`http://somewebsite.com/<arkproject_id>/<context_code>`
    gets just a context

`http://somewebsite.com/<arkproject_id>/<context_code>?<frag_type>=<attr>`
    gets the `<attr>` from the `<frag_type>` for the context

Note on geo components
.......................

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
............................

Django creates an abstraction layer of ARK's MySQL database; it's defined in
`arkaddons/core/arkmodels.py`. Only the tables containing actual archaeological
data useful to reconstruct the context structure have been mapped, leaving apart
all those tables related to the characteristics of the PHP application.


Stats
-----
A separate statistical application to dynamically query *any* archaeological (JSON) API
and create plots. It enables the user to extract a certain field or attribute from
an archaeological API for any context in the API, and moves it to a separate table.
Having a column for every attribute of all the contexts makes really easy to
perform simple and advanced queries on data.

Defining a project
..................

In the main page, `http:://somewebsite.com/stats/projects` add a new project,
defining some basic information. You will be able to get a detailed view of the
project in its page:  `http:://somewebsite.com/stats/project/<project_code>`.

Syncing the contexts
....................

In the project details page you find all the tools to start importing data in
the database. The first step is to synchronize the contexts available in the API
with those in the app database for the current project. Pressing the `Sync cxt`
button will open a modal.
The tool supports any kind of archaeological API, so it has no way to know
automatically how the context are placed in the JSON API. *We need to tell it
where to find a unique identifier for each context in the API's JSON.* This can
be done using a [JSON XPath](http://goessner.net/articles/JsonPath).


Installation
------------

    sudo apt-get install spatialite

    pip install virtualenvwrapper
    mkwirtualenv --python=python2.7 arkaddons
    workon arkaddons

    pip install -r requirements/base.txt

Starting with provided Spatialite db
....................................

Attached to this project comes a preconfigured Spatialite database, containing
all the necessary tables to use all the apps. Just copy the `default.db` file
from `misc` folder to `arkaddons`:

    cd arkaddons
    cp arkaddons/misc/default.db arkaddons/arkaddons/.

Start your own Spatialite db
............................

    cd arkaddons/arkaddons/arkaddons
    python manage.py syncdb
    spatialite default.db "SELECT InitSpatialMetaData();"
    python manage.py schemamigration appcore --initial
    python manage.py schemamigration appstats --initial
    python manage.py schemamigration appgeostat --initial
    python manage.py migrate

Independently of any of the above procedures, you have to rename the `__init__.py`
file in the `core` app before starting the server:

    cp appcore/core_init.py to appcore/__init__.py


FAQs
----
