#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install as _install

# Package meta-data.
NAME = 'watson_project'
DESCRIPTION = "Version Control demo for development environment"
URL = "https://github.azc.ext.hp.com/eason-chang/mlproject-development-template"
EMAIL = "eason.chang@hp.com"
AUTHOR = "Eason"
REQUIRES_PYTHON = ">=3.6.0"


# What packages are required for this module to be executed?
def list_reqs(fname="requirements.txt"):
    with open(fname) as fd:
        return fd.read().splitlines()


# The rest you shouldn't have to touch too much :)
# ------------------------------------------------
# Except, perhaps the License and Trove Classifiers!
# If you do change the License, remember to change the
# Trove Classifier for that!
long_description = DESCRIPTION

# Load the package's VERSION file as a dictionary.
about = {}
ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / 'watson_project'
with open(PACKAGE_DIR / "VERSION") as f:
    _version = f.read().strip()
    about["__version__"] = _version


# install the NLTK data in setup.py by overriding cmdclass with my own Install class
class Install(_install):
    def run(self):
        _install.do_egg_install(self)
        import nltk

        nltk.download("stopwords")


# Where the magic happens:
setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    cmdclass={"install": Install},
    install_requires=["nltk"],
    setup_requires=["nltk"],
    extras_require={},
    include_package_data=True,
    license="BSD-3",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
)