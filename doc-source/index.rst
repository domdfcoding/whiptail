===========================
whiptail
===========================

.. start short_desc

.. documentation-summary::
	:meta:

.. end short_desc

.. image:: https://coveralls.io/repos/github/domdfcoding/whiptail/badge.svg?branch=master
	:target: https://coveralls.io/github/domdfcoding/whiptail?branch=master
	:alt: Coverage

.. start shields

.. only:: html

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

	.. |docs| rtfd-shield::
		:project: whiptail
		:alt: Documentation Build Status

	.. |docs_check| actions-shield::
		:workflow: Docs Check
		:alt: Docs Check Status

	.. |actions_linux| actions-shield::
		:workflow: Linux
		:alt: Linux Test Status

	.. |actions_windows| actions-shield::
		:workflow: Windows
		:alt: Windows Test Status

	.. |actions_macos| actions-shield::
		:workflow: macOS
		:alt: macOS Test Status

	.. |actions_flake8| actions-shield::
		:workflow: Flake8
		:alt: Flake8 Status

	.. |actions_mypy| actions-shield::
		:workflow: mypy
		:alt: mypy status

	.. |requires| image:: https://dependency-dash.repo-helper.uk/github/domdfcoding/whiptail/badge.svg
		:target: https://dependency-dash.repo-helper.uk/github/domdfcoding/whiptail/
		:alt: Requirements Status

	.. |codefactor| codefactor-shield::
		:alt: CodeFactor Grade

	.. |pypi-version| pypi-shield::
		:project: whiptail-dialogs
		:version:
		:alt: PyPI - Package Version

	.. |supported-versions| pypi-shield::
		:project: whiptail-dialogs
		:py-versions:
		:alt: PyPI - Supported Python Versions

	.. |supported-implementations| pypi-shield::
		:project: whiptail-dialogs
		:implementations:
		:alt: PyPI - Supported Implementations

	.. |wheel| pypi-shield::
		:project: whiptail-dialogs
		:wheel:
		:alt: PyPI - Wheel

	.. |license| github-shield::
		:license:
		:alt: License

	.. |language| github-shield::
		:top-language:
		:alt: GitHub top language

	.. |commits-since| github-shield::
		:commits-since: v0.3.2
		:alt: GitHub commits since tagged version

	.. |commits-latest| github-shield::
		:last-commit:
		:alt: GitHub last commit

	.. |maintained| maintained-shield:: 2022
		:alt: Maintenance

	.. |pypi-downloads| pypi-shield::
		:project: whiptail-dialogs
		:downloads: month
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
---------------

.. start installation

.. installation:: whiptail-dialogs
	:pypi:
	:github:

.. end installation

You must also have the ``whiptail`` package installed on your system.

On Debian and derivatives this can be installed with:

.. prompt:: bash

	apt-get install whiptail


.. toctree::
	:hidden:

	Home<self>
	example
	docs
	contributing
	Source
	license

.. sidebar-links::
	:caption: Links
	:github:
	:pypi: whiptail-dialogs


.. start links

.. only:: html

	View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

	:github:repo:`Browse the GitHub Repository <domdfcoding/whiptail>`

.. end links
