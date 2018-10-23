from distutils.core import setup

packages = ['cricapi']

requires = [
    'requests',
]
setup(
  name = 'crciapi',
  packages = ['crciapi'], # this must be the same as the name above
  version = '1.0',
  description = 'The cricapi, Free to use, super-high bandwidth, high performance Cricket API. Targeted at Developers and Cricket lovers.',
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
