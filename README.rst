############################
cookiecutter-chrisapp |Logo| 
############################

|License| |Last Commit|

.. |Logo| image:: ../assets/logo_chris.png?raw=true
  :alt: ChRIS Logo
.. |License| image:: https://img.shields.io/github/license/fnndsc/cookiecutter-chrisapp.svg
  :alt: License
.. |Last Commit| image:: https://img.shields.io/github/last-commit/fnndsc/cookiecutter-chrisapp.svg
  :alt: Last Commit
  
A cookiecutter template for ChRIS plugin apps.


Abstract
========

This page describes how to get started with creating a ChRIS plugin. The first-time steps typically involve:

* Installing a python virtual environment for development.
* Using the *cookiecutter* Python module to set up a template project.
* Pushing your app to both Github and Docker Hub.

Background
==========

Before we begin, you should be familiar with these topics:

* git
* docker
* python

Beginners should read our `Introduction to Docker`_ and learn how to set up a `Python virtual environment`_.

.. _Introduction to Docker: https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Introduction-to-Docker
.. _Python virtual environment: https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Best-Practices#python-environments

ChRIS apps are known as plugins. They can be thought of as data processing modules.
Plugins are typically coded in Python (the app doesn't have to be Python, but non-Python
plugins are most easily deployed to the ChRIS platform using our ``ChrisApp`` Python wrapper/entrypoint).
In most cases ChRIS apps process data from an ``inputdir`` and save results in an ``outputdir``.
Importantly, ChRIS apps, since they often run in remote environments, have *NO GUI USER INTERFACES*.
All information pertinent to the plugin execution is supplied via command line arguments and/or data in the ``inputdir``.

::

                       ┌───────────────────┐
    /incoming data ───►│ ChRIS 'DS' plugin ├───► /outgoing results
                       └───────────────────┘

Requirements
============

* ``Python`` (version 3.5+) and ``pip`` (which is usually installed with Python)
* Latest ``Docker`` (version 17.04.0+) if you want to test your plugin's docker image and containers in your local machine.


Quickstart
==========

1. Install the cookiecutter tool::

    pip install -U cookiecutter


2. Generate a ChRIS plugin app project template::

    cookiecutter https://github.com/FNNDSC/cookiecutter-chrisapp.git

In running the above command, you will be prompted for an app project name. The app project name should be a valid python module name as described here https://www.python.org/dev/peps/pep-0008/#package-and-module-names.

The interactive script will ask you to choose between two types of ChRIS plugins.

i. **FS** (or **Feed Synthesis**) plugin app. These are **always** the first plugins in a Feed chain. They can be thought of as applications that primarily create ``outgoing`` results and do not have a preceding `incoming` directory. Often, an **FS** app will generate data in response to some user behavior (such as dragging and dropping files from the user's local context; or user querying a database for data; or even simply copying files within its container filesystem to the output directory). These plugins **only** enforce a single positional argument -- an output directory where the results of some *feed synthesis* event are stored. 

::

   ┌───────────────────┐
   │ ChRIS 'FS' plugin ├───► /outputdir
   └───────────────────┘

The ``outputdir`` of a plugin becomes the ``inputdir`` of the next plugin down the processing chain.


ii. **DS** (or **Data Synthesis**) plugin app. These are by far the most common plugins and enforce **two** positional arguments: an **input** directory (typically the result of a previous plugin's output) and an **output** directory.

::

                  ┌───────────────────┐
    /inputdir ───►│ ChRIS 'DS' plugin ├───► /outputdir
                  └───────────────────┘

The first plugin of a pipeline would always be a single **FS** plugin followed by a (possibly branched) chain of **DS** plugins creating files in the same single feed that was created by the root **FS** plugin. **Most of the time you will be creating a DS plugin when integrating your software application in ChRIS**.

Execution chains follow logically as linked list of an **FS** plugin followed by one or more **DS** plugins.

::

   ┌───────────────────┐  ┌─►/outputdir    ┌───────────────────┐  ┌─►/outputdir    ┌───────────────────┐  ┌─►/outputdir     
   │ ChRIS 'FS' plugin ├──┘      |     ┌──►│ ChRIS 'DS' plugin1├──┘      |     ┌──►│ ChRIS 'DS' plugin2├──┘
   └───────────────────┘     /inputdir─┘   └───────────────────┘     /inputdir─┘   └───────────────────┘       


3. Add your code.

4. Push to Github and Dockerhub. For help, read the `Beginner's Guide on our wiki <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Beginner%27s-Guide>`_.

Release Checklist
=================

Refer to https://github.com/FNNDSC/pl-simplefsapp (a simple **fs** plugin) and https://github.com/FNNDSC/pl-simpledsapp (a simple **ds** plugin) as examples
for guidance on getting started with your ChRIS plugin.

1. Do local test runs. Instructions for Docker can be found on the `wiki <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Beginner's-Guide#local-docker-build>`_.

2. Make sure dependency versions in ``requirements.txt`` and ``Dockerfile`` are correct.

3. Bump the version number in the ``setup.py``.

4. Finally please consult the `wiki <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki>`_ to learn how to register your app to ChRIS and the ChRIS store.

Notes
=====

A closer look at ``Dockerfile``

**Why is ``WORKDIR /usr/local/bin``**? The precedent is for a plugin to be run like

.. code::

    docker run fnndsc/pl-appname appname /in /out

i.e., executable scripts are expected to be found in the working directory.
Runtime settings are implied by ``Dockerfile``

.. code::

    docker run --entrypoint /usr/bin/python --workdir /usr/local/bin fnndsc/pl-appname appname /in /out

Here, the file ``/usr/local/bin/appname`` was created by python *setuptools* during ``pip install .``.
``--entrypoint /usr/bin/python`` (also denoted by the class attribute ``EXECSHELL`` in the ``ChrisApp``
subclass) is implied by the base image ``fnndsc/ubuntu-python3``.
