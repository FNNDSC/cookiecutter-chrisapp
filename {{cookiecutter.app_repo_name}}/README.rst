{{ cookiecutter.app_repo_name }}
================================

.. image:: https://img.shields.io/docker/v/fnndsc/{{ cookiecutter.app_repo_name }}
    :target: https://hub.docker.com/r/fnndsc/{{ cookiecutter.app_repo_name }}

.. image:: https://img.shields.io/github/license/fnndsc/{{ cookiecutter.app_repo_name }}
    :target: https://github.com/FNNDSC/{{ cookiecutter.app_repo_name }}/blob/master/LICENSE
{% if cookiecutter.publish_from_github_actions == 'yes' %}
.. image:: https://github.com/FNNDSC/{{ cookiecutter.app_repo_name }}/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/{{ cookiecutter.app_repo_name }}/actions
{% endif %}

.. contents:: Table of Contents


Abstract
--------

{{ cookiecutter.app_description }}


Description
-----------

``{{ cookiecutter.app_name }}`` is a ChRIS-based application that...


Usage
-----

.. code::

    python {{ cookiecutter.app_name }}.py
        [-h|--help]
        [--json] [--man] [--meta]
        [--savejson <DIR>]
        [-v|--verbosity <level>]
        [--version]
        <inputDir> <outputDir>


Arguments
~~~~~~~~~

.. code::

    [-h] [--help]
    If specified, show help message and exit.
    
    [--json]
    If specified, show json representation of app and exit.
    
    [--man]
    If specified, print (this) man page and exit.

    [--meta]
    If specified, print plugin meta data and exit.
    
    [--savejson <DIR>] 
    If specified, save json representation file to DIR and exit. 
    
    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.
    
    [--version]
    If specified, print version number and exit. 


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/{{ cookiecutter.app_repo_name }} {{ cookiecutter.app_name }} --man

Run
~~~

You need you need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u)                             \
        -v $(pwd)/in:/incoming -v $(pwd)/out:/outgoing      \
        fnndsc/{{ cookiecutter.app_repo_name }} {{ cookiecutter.app_name }}                        \
        /incoming /outgoing


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/{{ cookiecutter.app_repo_name }} .

Run unit tests:

.. code:: bash

    docker run --rm local/{{ cookiecutter.app_repo_name }} nosetests

Examples
--------

Put some examples here!


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
