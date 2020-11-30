========
Overview
========

.. start-badges
.. image:: https://travis-ci.com/andrew-alm/tensorfree.svg?branch=master
    :target: https://travis-ci.com/andrew-alm/tensorfree
.. image:: https://api.codeclimate.com/v1/badges/119b0928e6f2a18b0c01/maintainability
   :target: https://codeclimate.com/github/andrew-alm/tensorfree/maintainability
   :alt: Maintainability
.. image:: https://api.codeclimate.com/v1/badges/119b0928e6f2a18b0c01/test_coverage
   :target: https://codeclimate.com/github/andrew-alm/tensorfree/test_coverage
   :alt: Test Coverage
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
