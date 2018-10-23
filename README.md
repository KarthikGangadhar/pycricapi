# cricapi

[![image](https://img.shields.io/pypi/v/cricapi.svg)](https://pypi.org/project/cricapi/)
[![image](https://img.shields.io/pypi/l/cricapi.svg)](https://pypi.org/project/cricapi/)
[![image](https://img.shields.io/pypi/pyversions/cricapi.svg)](https://pypi.org/project/cricapi/)
[![codecov.io](https://codecov.io/github/karthikgangadhar/pycricapi/coverage.svg?branch=master)](https://codecov.io/github/karthikgangadhar/pycricapi)
[![image](https://img.shields.io/github/contributors/karthikgangadhar/pycricapi.svg)](https://github.com/karthikgangadhar/pycricapi/graphs/contributors)
<!-- [![image](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/kennethreitz) -->

The [cricapi](http://www.cricapi.com/), Free to use, super-high bandwidth, high performance Cricket API. Targeted at Developers and Cricket lovers.<br>
 The endpoints exposed are as follows:

 * `cricapi.cricket( )` provides live scrores  of ongoing match 
 * `cricapi.matches( )` provides upcoming match fixtures 
 * `cricapi.matchCalender( )` provides international fixtures
 * `cricapi.cricketScore( )` provides detailed score card of the match
 * `cricapi.playerStats( )` provides players carrer info and stats
 * `cricapi.fantasySummary( )` provides match info and stats
 * `cricapi.fantasySquad( )` provides team players info
 * `cricapi.playerFinder( )` provides players ids matching given name string
 
 In order to use the above endpoints, u need to have an api_key which can use generated by signing into [cricpapi](http://www.cricapi.com). For testing purpose can use test_api_key `"TESTKEY0273"`

Usage of Cricapi:

``` {.sourceCode .python}
>>> apikey = "TESTKEY0273"
>>> cricapi = Cricapi(apikey)
```
#### matches

```
>>> cricapi.matches()
{u'matches': [{u'toss_winner_team': u'Australia Women', u'team-2': u'Pakistan Women' ...}
```
#### cricket

```
>>> cricapi.cricket()
{u'v': u'1', u'cache': True, u'provider': {u'url': u'https://cricapi.com/', u'source': ...}
```
#### matchCalender

```
>>> cricapi.matchCalender()
{u'v': u'1', u'cache': True, u'provider': {u'url': u'https://cricapi.com/', u'source': ...}
```
#### cricketScore

```
>>> params = {'unique_id':1034809}
>>> cricapi.cricketScore(params)
{u'v': u'1', u'ttl': 3, u'team-2': u'India', u'matchStarted': True, u'team-1': u'England', u'provider': {u'url':u'https://cricapi.com/', u'source': u'Various', u'pubDate': u'2018-10-23T06:58:07.090Z'}, u'creditsLeft': 206}
```
#### playerStats

```
>>> params = {'pid':35320}
>>> cricapi.playerStats(params)
{u'profile': u"\n\nSachin Tendulkar has been the most complete batsman of his time, the most prolific runmaker of all time, and arguably the biggest cricket icon the game has ...}
```
#### fantasySquad

```
>>> params = {'unique_id':1034809}
>>> cricapi.fantasySquad(params)
{u'v': u'1', u'cache': True, u'provider': {u'url': u'https://cricapi.com/', u'source': u'Various', u'pubDate': u'2018-10-23T07:16:02.191Z'}, u'squad': [{u'players': [{u'pid': ... }
```
#### fantasySummary

```
>>> params = {'unique_id':1034809}
>>> cricapi.fantasySummary(params)
{u'type': u'Test', u'ttl': 7, u'provider': {u'url': u'https://cricapi.com/', u'source': u'Various', u'pubDate': u'2018-10-23T07:20:22.701Z'}, u'dateTimeGMT': u'2016-11-09T04:00:00.000Z', u'v': u'1', u'data': {u'toss_winner_tea ...}
```

#### playerFinder

```
>>> params = {'name':'sachin'}
>>> cricapi.playerFinder(params)
{u'ttl': 164, u'provider': {u'url': u'https://cricapi.com/', u'source': u'Various', u'pubDate': u'2018-10-23T07:24:47.164Z'}, u'v': u'1', u'data': [{u'fullName': u'Sachin Rana', u'pid': 33757, u'name': u'Sachin Rana'}, {u'full ...}
```

Cricapi officially supports Python 2.7 & 3.4–3.7, and runs great on
PyPy.

Installation
------------

To install Cricapi, simply use [pipenv](http://pipenv.org/) (or pip, of
course):

``` {.sourceCode .bash}
$ pipenv install cricapi
```

Documentation
-------------

Fantastic documentation is available at
<http://docs.python-cricapi.org/>.

How to Contribute
-----------------

1.  Check for open issues or open a fresh issue to start a discussion
    around a feature idea or a bug. There is a [Contributor
    Friendly](https://github.com/karthikgangadhar/pycricapi/issues?direction=desc&labels=Contributor+Friendly&page=1&sort=updated&state=open)
    tag for issues that should be ideal for people who are not very
    familiar with the codebase yet.
2.  Fork [the repository](https://github.com/karthikgangadhar/pycricapi) on
    GitHub to start making your changes to the **master** branch (or
    branch off of it).
3.  Write a test which shows that the bug was fixed or that the feature
    works as expected.
4.  Send a pull request and bug the maintainer until it gets merged and
    published. :) Make sure to add yourself to
    [AUTHORS](https://github.com/karthikgangadhar/pycricapi/blob/master/AUTHORS.rst).
