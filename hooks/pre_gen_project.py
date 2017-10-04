import re
import sys

if not '{{ cookiecutter.app_repo_name }}'.startswith('pl-'):
    print('ERROR: The app repo name must start with the "pl-" prefix')
    # Exit to cancel project
    sys.exit(1)

MODULE_REGEX = r'^[_a-zA-Z][_a-zA-Z0-9]+$'

module_name = '{{ cookiecutter.app_name }}'

if not re.match(MODULE_REGEX, module_name):
    print('ERROR: The app name (%s) is not a valid Python module name. Please do not use a - and use _ instead' % module_name)
    sys.exit(1)

