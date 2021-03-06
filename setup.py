#!/usr/bin/env python

with open("README.md", "r") as fh:
    long_description = fh.read()

import setuptools
from distutils.core import setup

setup(name='npfitsio',
      py_modules=['npfitsio'],
      version='0.1.0',
      license='lgpl-2.1',
      description='Fast 2D and 3D vector geometry module',
      long_description=long_description,
      long_description_content_type="text/markdown",
      author='Dov Grobgeld',
      author_email='dov.grobgeld@gmail.com',
      url='http://github.com/dov/npfitsio',
      keywords = ['fits'],
      install_requires=[            
          'numpy',
          'astropy',
      ],
      setup_requires=['wheel'],
      classifiers = [
          "Programming Language :: Python",
          "Programming Language :: Python :: 3",
          "Development Status :: 3 - Alpha",
          "Environment :: Other Environment",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: GNU Lesser General Public License v2 or later (LGPLv2+)",
          "Operating System :: OS Independent",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Scientific/Engineering :: Mathematics",
          ],
      )

