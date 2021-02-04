############################
cookiecutter-chrisapp |Logo| 
############################

|License| |Last Commit| |CI|

.. |Logo| image:: ../assets/logo_chris.png?raw=true
  :alt: ChRIS Logo
.. |License| image:: https://img.shields.io/github/license/fnndsc/cookiecutter-chrisapp.svg
  :alt: License
.. |Last Commit| image:: https://img.shields.io/github/last-commit/fnndsc/cookiecutter-chrisapp.svg
  :alt: Last Commit
.. |CI| image:: https://github.com/FNNDSC/cookiecutter-chrisapp/workflows/test/badge.svg
  :alt: Github Actions
  :target: https://github.com/FNNDSC/cookiecutter-chrisapp/actions

This repo provides a cookiecutter template for ChRIS plugin apps. Using this cookiecutter will allow you to *easily* create ChRIS plugins using a ``python`` template, with baked in support for easy containerization. Recommended additional steps guide you through setting up a github repo for your plugin, triggering automatic containerization of your plugin, and automatically publishing to ``dockerhub`` and a ``chrisstore``.

Note that though the plugin skeleton itself is a ``python`` construct, your application itself *does not have to be python*. Support for non-python applications is a more advanced topic with help provided elsewhere. Using this ``cookiecutter`` will require at the very minimum some python boilerplate to wrap around your application if it is non-python.

Background
==========

Before we begin, you should be familiar with these topics:

* ``git``
* ``docker``
* ``python``

For new developers, we recommend the following reading (seasoned developers can skip this):

* `What is a ChRIS plugin? <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/About-Plugins#what-is-a-chris-plugin>`
* `Introduction to Docker <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Introduction-to-Docker>`

Also, there is an *implicit* assumption in this documentation that you are on some OS that provides some flavour of a POSIX command line shell (``bash`` or ``zsh`` are recommended) on some UN*X env (typically some Linux distro or macOS). Please note that if you are on Windows, we have not tested these instructions on a default windows console (or PowerShell) and YMMV. We typically don't recommend using Windows for running/hosting a ChRIS system, but it could be used for developing plugins.

What will this cookiecutter do?
===============================

In a nutshell this cookiecutter, will at the very minimum:

* create a fully formed, but *empty* ChRIS plugin on your local filesystem (created in the directory you run the ``cookiecutter``);
* provide a Dockerfile that you can use to create containers of your plugin;
* provide some testing, dependency checking, and documentation files for you;

We also provide additional <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Quickstart> and instructions (and encouragement) for you to

* push your plugin code to ``github``;
* setup some additional hooks to allow for automatic building of containers for various architectures (``x86_64``, ``PowerPC``, and ``ARM``);


Getting Started
===============

Basic usage of this template requires the `cookiecutter <https://github.com/cookiecutter/cookiecutter>` tool and the assumption of a Python virtual environment (see <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Python-Woes#venv>). 

In a terminal, go to some directory that you want to contain the plugin code, and type

.. code::

    pip install -U cookiecutter
    cookiecutter https://github.com/FNNDSC/cookiecutter-chrisapp.git

When you run the above, you will be asked a series of questions. At the very least you should have a ``name`` in mind for your application, and provide this name when prompted. Note that other than the name, all the other questions can be simply skipped (by pressing ``enter``) if you so desire. Any entries you make (or don't make) can be easily modified after the ``cookiecutter`` has completed.

One final note of interset here concerns the ``Select app_type`` prompt of the ``cookiecutter``. Almost all plugins are of type ``ds`` (the default). Unless you have specific reason, you will most likely always be building ``ds`` type plugins (this is also the default). If you are doing this for the very first time, you will definitely want to code a ``ds`` plugin type. What are the plugin types? Take a look <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/About-Plugins>.

What do the questions in the ``cookiecutter`` mean? See `here <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/CookieCutter-Questions>`

First Steps
===========

Once you've answered all the ``cookiecutter`` questions you'll be quietly returned to the prompt. In your current directory/folder will be a new subdirectory of the following structure (assuming here that you called your plugin ``pl-app`` -- the default):

.. code::

    pl-app/
    ├── app
    │   ├── app.py
    │   ├── __init__.py
    │   ├── __main__.py
    │   └── tests
    │       ├── __init__.py
    │       └── test_app.py
    ├── Dockerfile
    ├── LICENSE
    ├── README.rst
    ├── requirements.txt
    └── setup.py
    
Your tree might look slightly different. Don't worry about that. 

From your perspective, the most important file is the ``app.py`` (and again, your name here will be different). Nonetheless, this constitutes the main entry point to your plugin code, and in the absolute minimum case is the only file you need to edit. Good practice here would be to also construct tests (off ``test_app.py``) and flesh out dependencies (``requirements.txt``) and write good documentation (``README.rst``).

You might be tempted to just try and run the ``app.py`` directly! We discourage this, simply because **this is python module, not a python app**. It needs to be imported into an actual standalone runnable entity. The ``cookiecutter`` has provided a ``setup.py`` for you for this very purpose which will automatically create a fully formed app (see next paragraph). 

Thus, at this juncture, you can in fact create and run that plugin *as is* without any additional coding on your part. It won't of course do much of anything useful, but it is a almost fully formed out-of-the-box and is just waiting to be given purpose. Note that *running* it is best performed by actually containerizing the plugin and running the docker image. That might sound complex, but the ``cookiecutter`` has already provided all the tools to enable this for you. You just need to follow the `steps <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Developer-Guide>`.

The Developer Guide provides instructions for two ways to run your plugin right now. Again, we recommend you taking the extra steps to construct a local docker image and run that, but you can also run your plugin *on the metal* so to speak by installing it to a python virtual environment (not really recommended).

The Developer Guide also provides some guidance on debugging.

Next Step -- get on git
=======================

Having created a plugin scaffolding and possibly created/run it as a test, you are now ready for the next recommended steps:

<https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Quickstart>:

* Create a repository on github and check this scaffolding in.
* Build a container image and manually push to Dockerhub

Automatic builds
=================

While optional, automatic builds are highly recommended. These can be setup so that whenever you `git push` changes to your source code, new container images will be automatically created for you and pushed to Dockerhub. These containers will by default be multi-arch.

<https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Automatic-Builds>

Note that you need to do nothing more once you have setup automatic builds. Each time you push changes to your code, at some point after that you will get an email from Dockerhub concerning the results of that build. As part of this process, whatever tests you have created (in `app_test.py`) will be executed and the results also returned to you. Note that an image is built and pushed to Dockerhub irrespective of your test results status.

Please review our `best practices <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Best-Practices>` regarding publication of ChRIS plugins.

Finally, the automatic build process is asynchronous from your perspective. Once you 

.. code::

    git push && git tag <someTag> && git push --tags
    
there will be no inidcation in your terminal that anything has happened other than the the `git` operations. In order to check on your builds, go to the `Actions` tab on the github page of your repo to monitor the state of the build process.

CODE
====

At this point you are ready to really start coding. See our <https://github.com/FNNDSC/cookiecutter-chrisapp/wiki/Coding-Guide> for some hints and strategies.


