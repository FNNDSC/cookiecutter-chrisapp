#                                                            _
# {{ cookiecutter.app_name }} {{ cookiecutter.app_type }} app
#
# (c) 2016 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os

# import the Chris app superclass
from chrisapp.base import ChrisApp


class {{ cookiecutter.app_python_class_name }}(ChrisApp):
    """
    {{ cookiecutter.app_description }}.
    """
    AUTHORS         = '{{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})'
    SELFPATH        = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC        = os.path.basename(__file__)
    EXECSHELL       = 'python3'
    TITLE           = '{{ cookiecutter.app_title }}'
    CATEGORY        = '{{ cookiecutter.app_category }}'
    TYPE            = '{{ cookiecutter.app_type }}'
    DESCRIPTION     = '{{ cookiecutter.app_description }}'
    DOCUMENTATION   = '{{ cookiecutter.app_documentation }}'
    VERSION         = '{{ cookiecutter.app_version }}'
    LICENSE         = 'Opensource (MIT)'
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MAX_CPU_LIMIT         = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT         = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT      = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT      = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT         = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT         = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Fill out this with key-value output descriptive info (such as an output file path
    # relative to the output dir) that you want to save to the output meta file when
    # called with the --saveoutputmeta flag
    OUTPUT_META_DICT = {}
 
    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        """

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """



# ENTRYPOINT
if __name__ == "__main__":
    app = {{ cookiecutter.app_python_class_name }}()
    app.launch()
