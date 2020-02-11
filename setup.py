#!/usr/bin/python
from setuptools import find_packages


import os
from setuptools import setup


with open("README.md") as readme_file:
    readme = readme_file.read()

setup(
    name="calci",
    version="0.1",
    author="Mugdha Dalal",
    author_email="mugdhadalal@gmail.com",
    url="https://github.com/mugdhadalal/calci",
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3 :: Only",
    ],
    install_requires=['fire', 'setuptools_scm'],
    entry_points={"console_scripts": ["calci=calci:main"]},
    long_description=readme,
    packages=find_packages(include=["calci"]),
)
