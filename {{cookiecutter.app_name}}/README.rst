##########
pl-dircopy
##########


Abstract
********

A Chris 'fs' plugin app to copy an entire directory into the output directory.

Run
***

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run -v /home:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-dircopy dircopy.py            \
            --dir /incoming /outgoing

The above will recursively copy the entire host ``/home`` dir to the container's ``/outgoing``
which in turn has been volume mapped to the host ``$(pwd)/out`` directory.

Make sure that the host ``$(pwd)/out`` directory is world writable!







