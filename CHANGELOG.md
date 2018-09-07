# Changelog
All notable changes to this project will be documented in this file.

This project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

<h2><a href="https://gitlab.com/dspechnikov/django-slugger/compare/v1.1.2...master">Unreleased</a></h2>

<h2><a href="https://gitlab.com/dspechnikov/django-slugger/compare/v1.1.1...v1.1.2">1.1.2</a> - 2018-09-07</h2>

### Fixed

* Added missing commit for #6 fix

<h2><a href="https://gitlab.com/dspechnikov/django-slugger/compare/v1.1.0...v1.1.1">1.1.1</a> - 2018-09-07</h2>

### Fixed
* Incorrect slug suffix generation if there are instances ending with the same slug -- #6 (thanks @folt)

<h2><a href="https://gitlab.com/dspechnikov/django-slugger/compare/v1.0.4...v1.1.0">1.1.0</a> - 2018-07-12</h2>

### Added
* Python 3.7 support -- #4

### Removed
* Python 3.5 support -- #5

<h2><a href="https://gitlab.com/dspechnikov/django-slugger/compare/v1.0.3...v1.0.4">1.0.4</a> - 2017-10-18</h2>

### Fixed
* Parent model unique_together constraint violated for multi-table inheritance
(see [#3](https://gitlab.com/dspechnikov/django-slugger/issues/3)).


<h2><a href="https://gitlab.com/dspechnikov/django-slugger/compare/v1.0.2...v1.0.3">1.0.3</a> - 2017-10-16</h2>

### Fixed
* Parent model instances aren't used for unique slug generation
(see [#2](https://gitlab.com/dspechnikov/django-slugger/issues/2)).


<h2><a href="https://gitlab.com/dspechnikov/django-slugger/compare/v1.0.1...v1.0.2">1.0.2</a> - 2017-10-11</h2>

### Added
* Package-level import shortcut for AutoSlugField.

### Fixed
* Slug is incorrectly generated for already saved object
(see [#1](https://gitlab.com/dspechnikov/django-slugger/issues/1)).


<h2>1.0.1 - 2017-10-03</h2>

### Added
* Single database query for slug generation.
* Support for all standard "unique_for" field attributes like *unique_for_date*.
* Support for model meta *unique_together* attribute.
* Support for custom "slugify" functions.
