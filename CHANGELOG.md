# Changelog
All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<h2><a href="https://gitlab.com/dspechnikov/django-slugger/compare/v1.0.2...master">Unreleased</a></h2>

### Fixed
* [#2](https://gitlab.com/dspechnikov/django-slugger/issues/2) -
Parent model instances aren't used for unique slug generation.

<h2><a href="https://gitlab.com/dspechnikov/django-slugger/compare/v1.0.1...v1.0.2">1.0.2</a> - 2017-10-11</h2>

### Added
* Package-level import shortcut for AutoSlugField.

### Fixed
* [#1](https://gitlab.com/dspechnikov/django-slugger/issues/1) -
Slug is incorrectly generated for already saved object.

<h2>1.0.1 - 2017-10-03</h2>

### Added
* Single database query for slug generation.
* Support for all standard "unique_for" field attributes like *unique_for_date*.
* Support for model meta *unique_together* attribute.
* Support for custom "slugify" functions.
