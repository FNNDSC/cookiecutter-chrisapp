from os import path
from setuptools import setup

with open(path.join(path.abspath(path.dirname(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = '{{ cookiecutter.app_name }}',
    # for best practices make this version the same as the VERSION class variable
    # defined in your ChrisApp-derived Python class
    version          = '{{ cookiecutter.app_version }}',
    description      = '{{ cookiecutter.app_description }}',
    long_description = readme,
    author           = '{{ cookiecutter.author_name }}',
    author_email     = '{{ cookiecutter.author_email }}',
    url              = '{{ cookiecutter.app_documentation }}',
    packages         = ['{{ cookiecutter.app_name }}'],
    install_requires = ['chrisapp~=1.1.6'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    scripts          = ['{{ cookiecutter.app_name }}/{{ cookiecutter.app_name }}.py'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.5',
)
