===========================
whiptail
===========================

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
	  - |travis| |actions_windows| |actions_macos| |codefactor|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| image:: https://img.shields.io/readthedocs/whiptail/latest?logo=read-the-docs
	:target: https://whiptail.readthedocs.io/en/latest/?badge=latest
	:alt: Documentation Status

.. |docs_check| image:: https://github.com/domdfcoding/whiptail/workflows/Docs%20Check/badge.svg
	:target: https://github.com/domdfcoding/whiptail/actions?query=workflow%3A%22Docs+Check%22
	:alt: Docs Check Status

.. |travis| image:: https://img.shields.io/travis/com/domdfcoding/whiptail/master?logo=travis
	:target: https://travis-ci.com/domdfcoding/whiptail
	:alt: Travis Build Status

.. |actions_windows| image:: https://github.com/domdfcoding/whiptail/workflows/Windows%20Tests/badge.svg
	:target: https://github.com/domdfcoding/whiptail/actions?query=workflow%3A%22Windows+Tests%22
	:alt: Windows Tests Status

.. |actions_macos| image:: https://github.com/domdfcoding/whiptail/workflows/macOS%20Tests/badge.svg
	:target: https://github.com/domdfcoding/whiptail/actions?query=workflow%3A%22macOS+Tests%22
	:alt: macOS Tests Status

.. |requires| image:: https://requires.io/github/domdfcoding/whiptail/requirements.svg?branch=master
	:target: https://requires.io/github/domdfcoding/whiptail/requirements/?branch=master
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

.. |commits-since| image:: https://img.shields.io/github/commits-since/domdfcoding/whiptail/v0.3.2
	:target: https://github.com/domdfcoding/whiptail/pulse
	:alt: GitHub commits since tagged version

.. |commits-latest| image:: https://img.shields.io/github/last-commit/domdfcoding/whiptail
	:target: https://github.com/domdfcoding/whiptail/commit/master
	:alt: GitHub last commit

.. |maintained| image:: https://img.shields.io/maintenance/yes/2020
	:alt: Maintenance

.. |pre_commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
	:target: https://github.com/pre-commit/pre-commit
	:alt: pre-commit

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
---------------

.. start installation

.. tabs::

	.. tab:: from PyPI

		.. prompt:: bash

			python3 -m pip install whiptail-dialogs --user


	.. tab:: from GitHub

		.. prompt:: bash

			python3 -m pip install git+https://github.com/domdfcoding/whiptail@master --user

.. end installation

You must also have the ``whiptail`` package installed on your system.

On Debian and derivatives this can be installed with:

.. prompt:: bash

	apt-get install whiptail


.. toctree::
	:hidden:

	Home<self>

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	API Reference<docs>
	Source
	Building

.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/whiptail>`__

.. end links
