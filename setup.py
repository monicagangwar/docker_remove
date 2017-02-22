from setuptools import setup, find_packages
import sys
import os

version = '1.0.2'

setup(name='docker_remove',
      version=version,
      description="Utility to easily remove Docker containers and Images through string matching",
      classifiers=[],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Docker',
      author='Monica Gangwar',
      author_email='monicagangwar10@gmail.com',
      url='https://github.com/monicagangwar/docker_remove',
      license='GPL-3.0',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=["argparse"],
      entry_points={
          'console_scripts': [
              'docker_remove=docker_remove.main:main',
          ]
      },

      )
