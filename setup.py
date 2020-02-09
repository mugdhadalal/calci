#!/usr/bin/env python3

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'calculator_project'
    entry_points={
        'console_scripts': [
            'calci = calci:main',
        ],
    packages = ['an_example_pypi_project', 'tests'],
    description = ("An demonstartion of calculator orogram"),
    platforms = ["Linux"],
    long_description=read('README')
    author = "Mugdha Dalal",
    author_email = "mugdhadalal@gmail.com",
    url = "https://github.com/mugdhadalal/calci",
)
