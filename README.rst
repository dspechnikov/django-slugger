django-slugger
==============

.. image:: https://gitlab.com/dspechnikov/django-slugger-draft/badges/master/pipeline.svg
    :alt: build status
    :target: https://gitlab.com/dspechnikov/django-slugger-draft/commits/master

.. image:: https://gitlab.com/dspechnikov/django-slugger-draft/badges/master/coverage.svg
    :alt: code coverage
    :target: https://gitlab.com/dspechnikov/django-slugger-draft/commits/master

Automatic slug field for your Django models.

Features
--------

* One query to rule them all. No database spam on model save.
* Supports all standard "unique_for" field attributes like *unique_for_date*.
* Supports model meta *unique_together*.
* Supports custom "slugify" functions.

How it works
------------

django-slugger provides ``AutoSlugField`` which value is automatically
generated if it is not filled manually. If the field has any "uniqueness"
constraint (``unique=True``, for example), numerical suffix will be used if
necessary to prevent constraint violation.

If generated slug exceeds field ``max_length``, slug value will be cut to
fit in. This does not apply to suffixed slugs. Increase ``max_length``
attribute value or use `custom slug template`_ if you need more space to
ensure slug uniqueness.

Installation
------------

.. code-block:: bash

    pip install django-slugger

Usage
-----

.. code-block:: python

    from slugger.fields import AutoSlugField

    class AutoSlugModel(models.Model):
        title = models.CharField(max_length=255)
        slug = AutoSlugField(populate_from='title')

Custom slug template
++++++++++++++++++++

By default, django-slugger will use Django slugify_ function
(combined with unidecode_ to handle non-ASCII characters). To use your own function,
specify it in ``slugify`` argument.

.. code-block:: python

    def custom_slugify(value):
        return 'custom-%s' % value

    class CustomAutoSlugModel(models.Model):
        title = models.CharField(max_length=255)
        slug = AutoSlugField(populate_from='title', slugify=custom_slugify)

.. note::

    ``slugify`` argument must be top-level named function.

Contributing
------------

Feel free to submit an issue_ or `merge request`_ for any feature ideas or
bug fixes.

.. _slugify: https://docs.djangoproject.com/en/1.11/ref/utils/#django.utils.text.slugify
.. _unidecode: https://pypi.python.org/pypi/Unidecode
.. _issue: https://gitlab.com/dspechnikov/django-slugger/issues
.. _merge request: https://gitlab.com/dspechnikov/django-slugger/merge_requests
