#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Setup file for wildcards package"""

from setuptools import setup
from os.path import abspath, dirname, join

dir=dirname(abspath(__file__))
description = open(join(dir,'description')).read()
readme = open(join(dir,'README.rst')).read()

setup(name='wildcards',
      version='0.0.1',
      description=description,
      long_description=readme,
      author='cancerhermit',
      author_email='cancerhermit@gmail.com',
      url='http://github.com/cancerhermit/wildcards.py/',
      py_modules = ["wildcards"],
      install_requires=[],
      keywords="wildcards fnmatch filter",
      classifiers=(
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Environment :: Console',

          'Natural Language :: English',

          'Programming Language :: Python',

          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Utilities'
      ),
      license="GPL"
)