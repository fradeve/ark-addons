.. arkaddons documentation master file, created by
   sphinx-quickstart on Sun Feb 17 11:46:20 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to arkaddons's documentation!
=====================================

This is a Django project to obtain statistical information from
an `ARK`_ (Archaeological Recording Kit) project.
It is aimed to mine data from archaeological databases and create customizable
visualizations, querying both text and geographical data.
It consists of separate tools, each one is a Django app; they could be activated
independently (although it could be useful activate them all together).

In ArkAddons, every app provides some new functions; some of these integrates
with other apps' functions, other simply add a new "module" in the main view.
Check out apps pages for more information.

.. _ARK: http://ark.lparchaeology.com

Contents:

.. toctree::
   :maxdepth: 2

   install
   Core app <app_core>
   Stats app <app_stats>
   deploy


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
