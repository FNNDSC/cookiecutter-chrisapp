{{ cookiecutter.app_repo_name }}
================================

.. image:: https://travis-ci.org/FNNDSC/{{ cookiecutter.app_name }}.svg?branch=master
    :target: https://travis-ci.org/FNNDSC/{{ cookiecutter.app_name }}

.. image:: https://img.shields.io/badge/python-3.8%2B-blue.svg
    :target: https://github.com/FNNDSC/{{ cookiecutter.app_repo_name }}/blob/master/setup.py

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


Python dependencies can be added to ``setup.py``.
After a successful build, track which dependencies you have installed by
generating the `requirements.txt` file.

.. code:: bash

    docker run --rm local/{{ cookiecutter.app_repo_name }} -m pip freeze > requirements.txt


For the sake of reproducible builds, be sure that ``requirements.txt`` is up to date before you publish your code.


.. code:: bash

    git add requirements.txt && git commit -m "Bump requirements.txt" && git push


Examples
--------

Put some examples here!


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
