################################
{{ cookiecutter.app_repo_name }}
################################


Abstract
********

{{ cookiecutter.app_description }}

Run
***

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run -v --rm $(pwd)/in:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/{{ cookiecutter.app_repo_name }} {{ cookiecutter.app_name }}.py            \
            /incoming /outgoing

This will ...

Make sure that the host ``$(pwd)/out`` directory is world writable!







