import os
import re
import sys

from codecs import open

from setuptools import setup
from distutils.core import setup

packages = ['cricapi']

requires = [
    'requests',
]

with open('README.md', 'r', 'utf-8') as f:
    readme = f.read()

setup(
  name = 'cricapi',
  packages = ['cricapi'], # this must be the same as the name above
  version = '1.2',
  description = 'The cricapi, Free to use, super-high bandwidth, high performance Cricket API. Targeted at Developers and Cricket lovers.',
  long_description=readme,
  long_description_content_type='text/markdown',
  author = 'kgangadhar',
  author_email = 'karthikg1643@gmail.com',
  url = 'https://github.com/KarthikGangadhar/pycricapi',
  download_url = 'https://github.com/KarthikGangadhar/pycricapi/tarball/1.0',
  keywords = ['cricket',
    'matchSchedule',
    'playerstat',
    'crciketScore',
    'matches',
    'fantasysquard',
    'fantasysummary',
    'playerfinder'], 
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],

)
