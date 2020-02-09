#!/usr/bin/python

import os
from setuptools import setup


def read(*paths):
    """ read files """
    with open(os.path.join(*paths), 'r') as filename:
        return filename.read()

setup(
    name="calci",
    version="0.2",
    long_description=(read('README.rst')),
    author="Mugdha Dalal",
    author_email="mugdhadalal@gmail.com",
    url=" https://github.com/mugdhadalal/calci",
    packages=['calci'],
    entry_points={
        'console_scripts': [
            'calci=calci:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4'
    ]
)

