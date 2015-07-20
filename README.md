[![Latest Version](https://img.shields.io/pypi/v/pandas_talib.svg)](https://pypi.python.org/pypi/pandas_talib/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/pandas_talib.svg)](https://pypi.python.org/pypi/pandas_talib/)
[![Wheel format](https://img.shields.io/pypi/wheel/pandas_talib.svg)](https://pypi.python.org/pypi/pandas_talib/)
[![License](https://img.shields.io/pypi/l/pandas_talib.svg)](https://pypi.python.org/pypi/pandas_talib/)
[![Development Status](https://img.shields.io/pypi/status/pandas_talib.svg)](https://pypi.python.org/pypi/pandas_talib/)
[![Downloads monthly](https://img.shields.io/pypi/dm/pandas_talib.svg)](https://pypi.python.org/pypi/pandas_talib/)
[![Requirements Status](https://requires.io/github/femtotrader/pandas_talib/requirements.svg?branch=master)](https://requires.io/github/femtotrader/pandas_talib/requirements/?branch=master)
[![Code Health](https://landscape.io/github/femtotrader/pandas_talib/master/landscape.svg?style=flat)](https://landscape.io/github/femtotrader/pandas_talib/master)
[![Codacy Badge](https://www.codacy.com/project/badge/1bf3606360934588ba764cca32210f52)](https://www.codacy.com/app/femto-trader/pandas_talib)
[![Build Status](https://travis-ci.org/femtotrader/pandas_talib.svg)](https://travis-ci.org/femtotrader/pandas_talib)


** Work in progress **

# pandas_talib
A Python Pandas implementation of technical indicators

Original version from:

- [Bruno Franca](https://github.com/brunogfranca)

- [panpanpandas](https://github.com/panpanpandas)

- [Peter Bakker](https://www.quantopian.com/users/51d125a71144e60865000044)

See also:

- [panpanpandas/ultrafinance](https://github.com/panpanpandas/ultrafinance)

- [llazzaro/analyzer](https://github.com/llazzaro/analyzer)

- <https://www.quantopian.com/posts/technical-analysis-indicators-without-talib-code>

If you are looking for a more complete set of technical indicators you might have a look at this TA-Lib Python wrapper: <https://github.com/mrjbq7/ta-lib>


## Install

A package is available and can be downloaded from PyPi and installed using:

	$ pip install pandas_talib

## Development

You can help to develop this library.

### Issues

You can submit issues using <https://github.com/femtotrader/pandas_talib/issues>

### Clone

You can clone repository to try to fix issues yourself using:

	$ git clone https://github.com/femtotrader/pandas_talib.git

### Run unit tests

Run all unit tests

	$ nosetests -s -v
	
Run a given test

	$ nosetests tests.test_pandas_talib:test_indicator_MA -s -v

### Run samples

Run `samples/main.py` (from project root directory)

	$ python samples/main.py

### Install development version

	$ python setup.py install
	
or

	$ sudo pip install git+git://github.com/femtotrader/pandas_talib.git

### Collaborating

- Fork repository
- Create a branch which fix a given issue
- Submit pull requests

<https://help.github.com/categories/collaborating/>