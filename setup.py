#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, find_packages


requirements = [
]

test_requirements = [
]

setup(
    name='algorithms2',
    version='0.1.0',
    packages=find_packages('src', exclude=["*.tests''", "*.tests.*", "tests.*", "tests"]),
    package_dir={'':'src'},
    include_package_data=False,
    install_requires=requirements,

    author='Jerry Kiely',
    author_email='jerry@cowboysmall.com',
    description='Algorithms Design and Analysis Part 2 contains all programming exercises for the Coursera course',
    keywords='algorithms2',
    url='https://github.com/cowboysmall/algorithms2',

    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],

    test_suite='tests',
    tests_require=test_requirements
)