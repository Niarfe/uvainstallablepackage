#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='shared',

      description='This package has shared components.',
      author='Greg Madden & Efrain Olivares',
      author_email='grm7q@virginia.edu',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
      license='LICENSE.txt',
    )
