=====
Stats
=====

This is a separate statistical application to dynamically query *any* archaeological (JSON) API
and create plots. It enables the user to extract a certain field or attribute from
an archaeological API for any context in the API, and moves it to a separate table.
Having a column for every attribute of all the contexts makes really easy to
perform simple and advanced queries on data.

Defining a project
^^^^^^^^^^^^^^^^^^

In the main page, ``http://somewebsite.com/stats/projects`` add a new project,
defining some basic information. You will be able to get a detailed view of the
project in its page:  ``http://somewebsite.com/stats/project/<project_code>``.

Syncing the contexts
^^^^^^^^^^^^^^^^^^^^

In the project details page you find all the tools to start importing data in
the database. The first step is to synchronize the contexts available in the API
with those in the app database for the current project. Pressing the `Sync cxt`
button will open a modal.
The tool supports any kind of archaeological API, so it has no way to know
automatically how the context are placed in the JSON API. *We need to tell it
where to find a unique identifier for each context in the API's JSON.* This can
be done using a `JSON XPath`_.

.. _`JSON XPath`: http://goessner.net/articles/JsonPath
