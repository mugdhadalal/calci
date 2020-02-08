#!/usr/bin/env python3
"""Calculator project"""
from setuptools import fire_packages, setup

setup(name = 'fire',
    version = '3.0',
    description = "Fire module.",
    long_description = long_description,
    platforms = ["Linux"],
    author="Mugdha Dalal",
    author_email="mugdhadalal@gmail.com",
    url="https://github.com/mugdhadalal/calci",
    packages=fire_packages()
)
