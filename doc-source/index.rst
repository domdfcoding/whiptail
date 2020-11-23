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
	  - |travis| |actions_windows| |actions_macos| |codefactor| |pre_commit_ci|
	* - PyPI
	  - |pypi-version| |supported-versions| |supported-implementations| |wheel|
	* - Activity
	  - |commits-latest| |commits-since| |maintained|
	* - Other
	  - |license| |language| |requires| |pre_commit|

.. |docs| rtfd-shield::
	:project: whiptail
	:alt: Documentation Build Status

.. |docs_check| actions-shield::
	:workflow: Docs Check
	:alt: Docs Check Status

.. |travis| actions-shield::
	:workflow: Linux Tests
	:alt: Linux Test Status

.. |actions_windows| actions-shield::
	:workflow: Windows Tests
	:alt: Windows Test Status

.. |actions_macos| actions-shield::
	:workflow: macOS Tests
	:alt: macOS Test Status

.. |requires| requires-io-shield::
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

.. |maintained| maintained-shield:: 2020
	:alt: Maintenance

.. |pre_commit| pre-commit-shield::
	:alt: pre-commit

.. |pre_commit_ci| pre-commit-ci-shield::
	:alt: pre-commit.ci status

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

.. toctree::
	:maxdepth: 3
	:caption: Documentation

	API Reference<docs>
	contributing
	Source

.. start links

View the :ref:`Function Index <genindex>` or browse the `Source Code <_modules/index.html>`__.

`Browse the GitHub Repository <https://github.com/domdfcoding/whiptail>`__

.. end links
