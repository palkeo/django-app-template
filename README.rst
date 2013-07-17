django-app-template
===================

What is it ?
------------


This is a template for creating a new reusable application for Django.
This uses the template feature added to the ``startapp`` command in Django 1.4. While
creating the app requires using Django 1.4 you can choose to support earlier versions
once it has been created.

To start a new app with this template::

    # Clone the repo
    git clone git://github.com/palkeo/django-app-template.git
    # Use the template
    django-admin.py startapp --template=django-app-template/template --extension=py,rst,in,cfg <app_name>


What Does This Give You
-----------------------------------

This template is indended to be used for a reusable application developed outside
of a Django project. Beyond the standard ``<app_name>/__init__.py``, ``<app_name>/models.py``,
``<app_name>/tests.py`` and ``<app_name>/views.py`` this template will create:

- README.rst - Some minor layout to get you started
- setup.py - A starting point for packaging your app
- AUTHORS - Add your name here
- LICENSE - Add a license here
- quicktest.py - Simple helper for running the application tests
- .gitignore - Just to save you a few key strokes


What To Do Next
-----------------------------------

This template gives you a good starting point for your application layout but there
are still some pieces of information to fill out:

- Write your app and tests
- Fill in the ``<app_name>/__init__.py`` doc string and ``__version__``
- Pick a license and add author names
- Write a more complete README
- Adjust the meta information in the ``setup.py``

You should also consider using `Sphinx <http://sphinx.pocoo.org/>`_ 
to create a more complete set of documentation. For than you can install Sphinx
and run the quickstart::

    # Install Sphinx
    pip install sphinx
    # Run the quickstart to create docs in docs/
    # Most other default answers should be fine
    sphinx-quickstart

When you are ready to upload your app to the Python Package Index (PyPi) you
can do that using the ``setup.py`` created with this template::

    # Register you package name and meta data (This is done once)
    python setup.py register
    # Create a release and upload it (This is done with every new version)
    python setup.py sdist upload


Licensing
---------

Please see the LICENSE file.

.. image:: http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-2.png
   :target: http://www.wtfpl.net/


Contacts
--------

Please see the AUTHORS file.
