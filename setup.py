#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Embarkchina Development Team.

from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='embarkTooks',
    version='0.0.1',
    description='tools for pgcontents',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/embarkchina/embarkTools',
    auther='Kerwin Sun',
    auther_email='sunkaihuisos@gmail.com',
    license='2 Clause BSD',
    packages=find_packages(),
    install_requires=['pgcontents', 'sqlalchemy', 'pandas'],
    include_package_data=True,
)
