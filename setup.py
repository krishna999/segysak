#!/usr/bin/python
# -*- coding: utf8 -*-+

from setuptools import setup
from setuptools import find_packages

long_description = '''
The SEG-Y File Swiss Army Knife (SEGY-SAK) is a package developed for
manipulating and transform SEG-Y Seismic Data.
'''

setup(name='segysak',
      version='0.1a',
      description='SEG-Y Seismic Data Inspection and Manipulation Tools',
      long_description=long_description,
      author='Tony Hallam',
      author_email='arh5@hw.ac.uk',
      url='https://github.com/trhallam/segysak',
      license='GPL3',
      install_requires=['numpy',
                        'pandas',
                        'segyio',
                        'xarray',
                        'netCDF4'],
      packages=find_packages(),
      #add command line scripts here
      entry_points = {
            'console_scripts': ['segysak=segysak.command_line:main']
      })
