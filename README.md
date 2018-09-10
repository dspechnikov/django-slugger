# django-slugger

[![pipeline status](https://gitlab.com/dspechnikov/django-slugger/badges/master/pipeline.svg)](https://gitlab.com/dspechnikov/django-slugger/commits/master)
[![coverage report](https://gitlab.com/dspechnikov/django-slugger/badges/master/coverage.svg)](https://gitlab.com/dspechnikov/django-slugger/commits/master)
[![pypi version](https://img.shields.io/pypi/v/django-slugger.svg)](https://pypi.python.org/pypi/django-slugger)
[![license](https://img.shields.io/pypi/l/django-slugger.svg)](./LICENSE)
[![python versions](https://img.shields.io/pypi/pyversions/django-slugger.svg)](https://www.python.org/)
[![django versions](https://img.shields.io/badge/django-1.11,%202.0,%202.1-blue.svg)](https://www.djangoproject.com/)

Automatic slug field for Django models.

## Features

- One query to rule them all. No database spam on model save.
- Supports all standard `unique_for` field attributes like `unique_for_date`.
- Supports model meta `unique_together`.
- Supports custom "slugify" functions.

## How it works

django-slugger provides `AutoSlugField` which value is automatically
generated if it is not filled manually. If the field has any "uniqueness"
constraint (`unique=True`, for example), numerical suffix will be used if
necessary to prevent constraint violation.

If generated slug exceeds field `max_length`, slug value will be cut to
fit in. This does not apply to suffixed slugs. Increase `max_length`
attribute value or use [custom slug template](#custom-slug-template) if you need 
more space to ensure slug uniqueness.

## Installation

```bash
pip install django-slugger
```

## Usage

```python
from slugger import AutoSlugField

class AutoSlugModel(models.Model):
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='title')
```

### Custom slug template

By default, django-slugger will use Django [slugify] function
(combined with [unidecode] to handle non-ASCII characters). To use your own function,
specify it in `slugify` argument.

```python
    def custom_slugify(value):
        return 'custom-%s' % value

    class CustomAutoSlugModel(models.Model):
        title = models.CharField(max_length=255)
        slug = AutoSlugField(populate_from='title', slugify=custom_slugify)
```

Note: `slugify` argument must be top-level named function.

[slugify]: https://docs.djangoproject.com/en/2.1/ref/utils/#django.utils.text.slugify
[unidecode]: https://pypi.python.org/pypi/Unidecode
