========
arktools
========

This project is a Django web interface to obtain statistical informations from an ARK (Archaeological Recording Kit) project.
It is aimed to mine data from archaeological databases and create customizable visualizations.

Install
-------

* virtualenv
* requirements

* syncdb
* manage.py schemamigration core --initial
* manage.py migrate

* cp misc/core_init.py to core/__init__.py
