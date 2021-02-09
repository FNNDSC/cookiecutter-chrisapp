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

# from https://github.com/tonistiigi/binfmt#build-test-image
available_platforms = [
    'linux/amd64',
    'linux/arm64',
    'linux/riscv64',
    'linux/ppc64le',
    'linux/s390x',
    'linux/386',
    'linux/arm/v7',
    'linux/arm/v6'
]

platforms_input = '{{ cookiecutter.platforms }}'
platforms_delim = ',' if ',' in platforms_input else '\n'

for platform_name in platforms_input.split(platforms_delim):
    if '/' not in platform_name:
        print(f'ERROR: platform "{platform_name}" does not match the form "os/arch"')
        print('hint: platforms is string input, not multiple choice')
        sys.exit(1)
    if platform_name not in available_platforms:
        print(f'WARNING: platform "{platform_name}" is unsupported')
