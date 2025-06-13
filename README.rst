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
	  - |docs| |docs_check|
	* - Tests
	  - |actions_linux| |actions_windows| |actions_macos|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained| |pypi-downloads|
	* - QA
	  - |codefactor| |actions_flake8| |actions_mypy|
	* - Other
	  - |license| |language| |requires|

.. |docs| image:: https://img.shields.io/readthedocs/whiptail/latest?logo=read-the-docs
	:target: https://whiptail.readthedocs.io/en/latest
	:alt: Documentation Build Status

.. |docs_check| image:: https://github.com/domdfcoding/whiptail/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/whiptail/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |actions_linux| image:: https://github.com/domdfcoding/whiptail/workflows/Linux/badge.svg
	:target: https://github.com/domdfcoding/whiptail/actions?query=workflow%3A%22Linux%22
	:alt: Linux Test Status

.. |actions_windows| image:: https://github.com/domdfcoding/whiptail/workflows/Windows/badge.svg
	:target: https://github.com/domdfcoding/whiptail/actions?query=workflow%3A%22Windows%22
	:alt: Windows Test Status

.. |actions_macos| image:: https://github.com/domdfcoding/whiptail/workflows/macOS/badge.svg
	:target: https://github.com/domdfcoding/whiptail/actions?query=workflow%3A%22macOS%22
	:alt: macOS Test Status

.. |actions_flake8| image:: https://github.com/domdfcoding/whiptail/workflows/Flake8/badge.svg
	:target: https://github.com/domdfcoding/whiptail/actions?query=workflow%3A%22Flake8%22
	:alt: Flake8 Status

.. |actions_mypy| image:: https://github.com/domdfcoding/whiptail/workflows/mypy/badge.svg
	:target: https://github.com/domdfcoding/whiptail/actions?query=workflow%3A%22mypy%22
	:alt: mypy status

.. |requires| image:: https://dependency-dash.repo-helper.uk/github/domdfcoding/whiptail/badge.svg
	:target: https://dependency-dash.repo-helper.uk/github/domdfcoding/whiptail/
	:alt: Requirements Status

.. |codefactor| image:: https://img.shields.io/codefactor/grade/github/domdfcoding/whiptail?logo=codefactor
	:target: https://www.codefactor.io/repository/github/domdfcoding/whiptail
	:alt: CodeFactor Grade

.. |pypi-version| image:: https://img.shields.io/pypi/v/whiptail-dialogs
	:target: https://pypi.org/project/whiptail-dialogs/
	:alt: PyPI - Package Version

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/whiptail-dialogs?logo=python&logoColor=white
	:target: https://pypi.org/project/whiptail-dialogs/
	:alt: PyPI - Supported Python Versions

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/whiptail-dialogs
	:target: https://pypi.org/project/whiptail-dialogs/
	:alt: PyPI - Supported Implementations

.. |wheel| image:: https://img.shields.io/pypi/wheel/whiptail-dialogs
	:target: https://pypi.org/project/whiptail-dialogs/
	:alt: PyPI - Wheel

.. |license| image:: https://img.shields.io/github/license/domdfcoding/whiptail
	:target: https://github.com/domdfcoding/whiptail/blob/master/LICENSE
	:alt: License

.. |language| image:: https://img.shields.io/github/languages/top/domdfcoding/whiptail
	:alt: GitHub top language

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/whiptail/v0.4.1
	:target: https://github.com/domdfcoding/whiptail/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/whiptail
	:target: https://github.com/domdfcoding/whiptail/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2025
	:alt: Maintenance

.. |pypi-downloads| image:: https://img.shields.io/pypi/dm/whiptail-dialogs
	:target: https://pypi.org/project/whiptail-dialogs/
	:alt: PyPI - Downloads

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
