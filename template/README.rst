{{ app_name }}
=================

.. image:: https://travis-ci.org/{{ author_slug }}/{{ app_name }}.png
    :target: https://travis-ci.org/{{ author_slug }}/{{ app_name }}

.. image:: https://coveralls.io/repos/{{ author_slug }}/{{ app_name }}/badge.png
    :target: https://coveralls.io/r/{{ author_slug }}/{{ app_name }}


What is it ?
------------

This is a template for a Django application.

Example
-------

.. code-block:: python

    # That's how you use your app


Installation
------------

The application doesn't have any special requirement.

It have been tested with Django 1.3, 1.4 and 1.5, using python 2.6 and 2.7.
It is also compatible with python 3, using Django 1.5.


Documentation
-------------

The documentation is available `here <http://{{ app_name }}.readthedocs.org>`_.


Licensing
---------

Please see the LICENSE file.

Contacts
--------

Please see the AUTHORS file.

{% if logo and homepage %}
.. image:: {{ logo }}
    :target: {{ homepage }}
{% endif %}
