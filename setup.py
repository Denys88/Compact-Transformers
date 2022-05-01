"""Setup script for cct"""

import sys
import os
import pathlib

from setuptools import setup, find_packages
# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()
print(find_packages())

setup(name='cct',
      long_description=README,
      long_description_content_type="text/markdown",
      url="https://github.com/SHI-Labs/Compact-Transformers",
      packages = ['cct',],
      package_data={'cct':['*','*/*','*/*/*','*/*/*/*']},
      version='1.0.0',
      author='',
      author_email='',
      license="MIT",
      classifiers=[
            "Apache License 2.0"
      ],
      include_package_data=True,
      install_requires=[
            'torch>=1.7.0',
            'numpy>=1.16.0',
      ],
      )
