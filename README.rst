========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis|
        |
        | |codeclimate|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/tensorfree/badge/?style=flat
    :target: https://readthedocs.org/projects/tensorfree
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/andrew-alm/tensorfree.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/andrew-alm/tensorfree

.. |codeclimate| image:: https://codeclimate.com/github/andrew-alm/tensorfree/badges/gpa.svg
   :target: https://codeclimate.com/github/andrew-alm/tensorfree
   :alt: CodeClimate Quality Status

.. |version| image:: https://img.shields.io/pypi/v/tensorfree.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/tensorfree

.. |wheel| image:: https://img.shields.io/pypi/wheel/tensorfree.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/tensorfree

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/tensorfree.svg
    :alt: Supported versions
    :target: https://pypi.org/project/tensorfree

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/tensorfree.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/tensorfree

.. |commits-since| image:: https://img.shields.io/github/commits-since/andrew-alm/tensorfree/v0.0.0.svg
    :alt: Commits since latest release
    :target: https://github.com/andrew-alm/tensorfree/compare/v0.0.0...master



.. end-badges

Update this a little later

* Free software: MIT license

Installation
============

::

    pip install tensorfree

You can also install the in-development version with::

    pip install https://github.com/andrew-alm/tensorfree/archive/master.zip


Documentation
=============


https://tensorfree.readthedocs.io/


Development
===========

To run all the tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
