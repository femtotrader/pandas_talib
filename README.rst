|Latest Version| |Supported Python versions| |Wheel format| |License|
|Development Status| |Downloads monthly| |Requirements Status| |Code
Health| |Codacy Badge| |Build Status|

\*\* Work in progress \*\*

pandas\_talib
=============

A Python Pandas implementation of technical indicators

Original version from:

-  `Bruno Franca <https://github.com/brunogfranca>`__

-  `panpanpandas <https://github.com/panpanpandas>`__

-  `Peter
   Bakker <https://www.quantopian.com/users/51d125a71144e60865000044>`__

Contributors

-  `Yao Hong Kok <https://github.com/yaohongkok>`__
- `Leonardo Lazzaro <https://github.com/llazzaro>`__
- `and all... <https://github.com/femtotrader/pandas_talib/graphs/contributors>`__

See also:

-  `panpanpandas/ultrafinance <https://github.com/panpanpandas/ultrafinance>`__

-  `llazzaro/analyzer <https://github.com/llazzaro/analyzer>`__

-  https://www.quantopian.com/posts/technical-analysis-indicators-without-talib-code

If you are looking for a more complete set of technical indicators you
might have a look at this TA-Lib Python wrapper:
https://github.com/mrjbq7/ta-lib

Development
-----------

You can help to develop this library.

Issues
~~~~~~

You can submit issues using
https://github.com/femtotrader/pandas_talib/issues

Clone
~~~~~

You can clone repository to try to fix issues yourself using:

::

    $ git clone https://github.com/femtotrader/pandas_talib.git

Run unit tests
~~~~~~~~~~~~~~

Follow instructions from TA-Lib and install it:

https://github.com/mrjbq7/ta-lib

Run all unit tests

::

    $ nosetests -s -v

Run a given test

::

    $ nosetests tests.test_pandas_talib:test_indicator_MA -s -v

Run samples
~~~~~~~~~~~

Run ``samples/main.py`` (from project root directory)

::

    $ python samples/main.py

Install development version
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

    $ python setup.py install

or

::

    $ sudo pip install git+https://github.com/femtotrader/pandas_talib.git

Known Issues
~~~~~~~~~~~~~

- The method ROC is currently not accurate yet.

Collaborating
~~~~~~~~~~~~~

-  Fork repository
-  Create a branch which fix a given issue
-  Submit pull requests

https://help.github.com/categories/collaborating/

.. |Latest Version| image:: https://img.shields.io/pypi/v/pandas_talib.svg
   :target: https://pypi.python.org/pypi/pandas_talib/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/pandas_talib.svg
   :target: https://pypi.python.org/pypi/pandas_talib/
.. |Wheel format| image:: https://img.shields.io/pypi/wheel/pandas_talib.svg
   :target: https://pypi.python.org/pypi/pandas_talib/
.. |License| image:: https://img.shields.io/pypi/l/pandas_talib.svg
   :target: https://pypi.python.org/pypi/pandas_talib/
.. |Development Status| image:: https://img.shields.io/pypi/status/pandas_talib.svg
   :target: https://pypi.python.org/pypi/pandas_talib/
.. |Downloads monthly| image:: https://img.shields.io/pypi/dm/pandas_talib.svg
   :target: https://pypi.python.org/pypi/pandas_talib/
.. |Requirements Status| image:: https://requires.io/github/femtotrader/pandas_talib/requirements.svg?branch=master
   :target: https://requires.io/github/femtotrader/pandas_talib/requirements/?branch=master
.. |Code Health| image:: https://landscape.io/github/femtotrader/pandas_talib/master/landscape.svg?style=flat
   :target: https://landscape.io/github/femtotrader/pandas_talib/master
.. |Codacy Badge| image:: https://www.codacy.com/project/badge/1bf3606360934588ba764cca32210f52
   :target: https://www.codacy.com/app/femto-trader/pandas_talib
.. |Build Status| image:: https://travis-ci.org/femtotrader/pandas_talib.svg
   :target: https://travis-ci.org/femtotrader/pandas_talib
