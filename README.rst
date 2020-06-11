====================
whiptail
====================

.. start short_desc

**Use whiptail to display dialog boxes from Python scripts.**

.. end short_desc

.. image:: https://coveralls.io/repos/github/domdfcoding/whiptail/badge.svg?branch=master
	:target: https://coveralls.io/github/domdfcoding/whiptail?branch=master
	:alt: Coverage


.. start shields 

.. list-table::
	:stub-columns: 1
	:widths: 10 90

	* - Docs
	  - |docs|
	* - Tests
	  - |travis| |requires| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Other
	  - |license| |language| |commits-since| |commits-latest| |maintained| 

.. |docs| image:: https://img.shields.io/readthedocs/whiptail/latest?logo=read-the-docs
	:target: https://whiptail.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/whiptail/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/whiptail
	:alt: Travis Build Status

.. |requires| image:: https://requires.io/github/domdfcoding/whiptail/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/whiptail/requirements/?branch=master
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/whiptail?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/whiptail
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/whiptail-dialogs
	:target: https://pypi.org/project/whiptail-dialogs/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/whiptail-dialogs
	:target: https://pypi.org/project/whiptail-dialogs/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/whiptail-dialogs
	:target: https://pypi.org/project/whiptail-dialogs/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/whiptail-dialogs
	:target: https://pypi.org/project/whiptail-dialogs/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/whiptail
	:alt: License
	:target: https://github.com/domdfcoding/whiptail/blob/master/LICENSE

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/whiptail
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/whiptail/v0.3.1dev
	:target: https://github.com/domdfcoding/whiptail/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/whiptail
	:target: https://github.com/domdfcoding/whiptail/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. end shields


``whiptail`` is a library that will let you present a variety of questions or
display messages using dialog boxes from a Python script.

Currently, these types of dialog boxes are implemented:

* yes/no box
* menu box
* input box
* message box
* text box
* info box
* checklist box
* radiolist box
* gauge box
* password box


Installation
--------------

.. start installation

``whiptail`` can be installed from PyPI.

To install with ``pip``:

.. code-block:: bash

	$ python -m pip install whiptail-dialogs

.. end installation

You must also have the ``whiptail`` package installed on your system.

On Debian and derivatives this can be installed with:

.. code-block:: bash

	$ apt-get install whiptail
