
import sys
import os


# Make sure we are running python3.5+
if 10 * sys.version_info[0]  + sys.version_info[1] < 35:
    sys.exit("Sorry, only Python 3.5+ is supported.")

from setuptools import setup


def readme():
    print("Current dir = %s" % os.getcwd())
    print(os.listdir())
    with open('README.rst') as f:
        return f.read()

setup(
      name             =   '{{ cookiecutter.app_name }}',
      # for best practices make this version the same as the VERSION class variable
      # defined in your main plugin app class
      version          =   '{{ cookiecutter.app_version }}',
      description      =   '{{ cookiecutter.app_description }}',
      long_description =   readme(),
      author           =   '{{ cookiecutter.author_name }}',
      author_email     =   '{{ cookiecutter.author_email }}',
      url              =   '{{ cookiecutter.app_documentation }}',
      packages         =   ['{{ cookiecutter.app_name }}'],
      install_requires =   ['chrisapp', 'pudb'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['{{ cookiecutter.app_name }}/{{ cookiecutter.app_name }}.py'],
      license          =   'MIT',
      zip_safe         =   False
     )
