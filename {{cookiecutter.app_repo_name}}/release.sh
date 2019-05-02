#!/bin/bash

G_SYNOPSIS="

 NAME

	release.sh

 SYNOPSIS

	release.sh <ver> [--pypi]

 ARGS

	<ver>
	A version string. For best practices make this version the same as
	the VERSION class variable defined in your main plugin app class.

	--pypi
	Optional flag to also upload the new version to PyPI.

 DESCRIPTION

	release.sh is a simple helper script to tag and upload a new version of the plugin
	app to Github. If --pypi is passed then the new version is also uploaded to PyPI
	(Python Package Index).


"

if [[ "$#" -eq 0 ]] || [[ "$#" -gt 2 ]]; then
    echo "$G_SYNOPSIS"
    exit 1
fi
VER=$1
if [[ "$#" -eq 2 ]]; then
    if [[ "$1" != '--pypi' ]] && [[ "$2" != '--pypi' ]]; then
        echo "$G_SYNOPSIS"
        exit 1
    fi
    if [[ "$1" == '--pypi' ]]; then
        VER=$2
    fi
fi
if [[ $VER =~ ^[0-9.]+$ ]]; then
    echo Pushing $VER to Github ...
    git add -A
    git commit -m "v${VER}"
    git push origin master
    git tag $VER
    git push origin --tags
else
    echo "Invalid version number format $VER."
    exit 1
fi
if [[ "$#" -eq 2 ]]; then
    echo pushing $VER to PyPI ...
    rstcheck README.rst
    python3 setup.py sdist
    twine upload dist/{{ cookiecutter.app_name }}-${VER}.tar.gz
fi
