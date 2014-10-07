#!/usr/bin/env python
# -*- coding:utf8 -*-
"""Setup Script
"""
from __future__ import unicode_literals
import os
import sys
import codecs
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    # http://pytest.org/latest/goodpractises.html?highlight=setup#integration-with-setuptools-test-commands
    user_options = []

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--pep8',
            '--cov-report', 'term-missing',
            '--cov', 'sweaper',
        ]
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


here = os.path.abspath(os.path.dirname(__file__))
sys.path.append(here)

with codecs.open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    README = f.read()

setup(
    name='python-chatwork',
    version='0.0.1',
    description='python chatwork-api client library',
    long_description=README + '\n\n',
    classifiers=[
        'Programming Language :: Python',
    ],
    author='attakei',
    author_email='attakei@gmail.com',
    url='https://github.com/attakei/python-chatwork',
    keywords='',
    packages=find_packages(exclude=['tests', ]),
    include_package_data=True,
    zip_safe=False,
    tests_require=[
        'pytest-pep8',
        'pytest-cov',
        'pytest',
    ],
    install_requires=[],
    cmdclass={'test': PyTest},
)
