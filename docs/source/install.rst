=======
Install
=======

.. code-block:: bash

    sudo apt-get install spatialite

    pip install virtualenvwrapper
    mkwirtualenv --python=python2.7 arkaddons
    workon arkaddons

    pip install -r requirements/base.txt

Keep an eye on Python version
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

ArkAddons runs on Python 2.7. There is a known issue about Python 2.7, SpatiaLite
and PySQLite2, as reported on `GeoDjango`_ docs. For this reason the `pysqlite`
package has not been included among the requirements, you will have to install
it manually in the virtualenv: just follow the instructions as per above link.

.. _GeoDjango: https://docs.djangoproject.com/en/1.6/ref/contrib/gis/install/spatialite/#pysqlite2

Starting with provided Spatialite db
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Attached to this project comes a preconfigured Spatialite database, containing
all the necessary tables to use all the apps. Just copy the ``default.db`` file
from ``misc`` folder to ``arkaddons``:

.. code-block:: bash

    cd arkaddons
    cp arkaddons/misc/default.db arkaddons/arkaddons/.

Default username: `admin`, password: `admin`.

Start your own Spatialite db
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: bash

    cd arkaddons/arkaddons/arkaddons
    spatialite arkaddons/default.db "SELECT InitSpatialMetaData();"
    python manage.py schemamigration appcore --initial
    python manage.py schemamigration appstats --initial
    python manage.py schemamigration appgeostat --initial
    python manage.py syncdb --migrate

Independently of any of the above procedures, you have to rename the ``__init__.py``
file in the ``core`` app before starting the server:

.. code-block:: bash

    cp appcore/core_init.py to appcore/__init__.py
