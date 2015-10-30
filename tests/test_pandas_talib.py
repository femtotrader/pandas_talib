#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import pandas as pd
import numpy as np
import talib
from pandas_talib import (
    MA,
    MOM,
    ATR,
)
# def test_pandas_talib():
#    raise(NotImplementedError)

basepath = os.path.dirname(__file__)
filename = os.path.join(basepath, "..", "data", "AAPL_GOOGL_IBM_20140101_20141201.xls")
d = pd.read_excel(filename, sheetname=None)
panel = pd.Panel.from_dict(d)
# print(panel.loc['Open','2014-02-03','AAPL'])
panel = panel.iloc[:, 1:, :]
panel.major_axis.name = "Date"
# print(panel)

df = panel.loc[:, :, 'AAPL']


def test_indicator_MA():
    n = 3
    price = 'Close'
    result = MA(df, n)
    isinstance(result, pd.DataFrame)
    expected = talib.MA(df[price].values, timeperiod=n)
    np.testing.assert_almost_equal(result.values, expected)

"""
def test_indicator_EMA():
    n = 3
    price = 'Close'
    result = EMA(df, n)
    isinstance(result, pd.DataFrame)
    expected = talib.EMA(df[price].values, timeperiod=n)
    np.testing.assert_almost_equal(result.values, expected)
"""


def test_indicator_MOM():
    n = 3
    price = 'Close'
    result = MOM(df, n)
    isinstance(result, pd.DataFrame)
    expected = talib.MOM(df[price].values, timeperiod=n)
    np.testing.assert_almost_equal(result.values, expected)

"""
def test_indicator_ROC():
    n = 3
    price = 'Close'
    result = ROC(df, n)
    isinstance(result, pd.DataFrame)
    expected = talib.ROC(df[price].values, timeperiod=n)
    np.testing.assert_almost_equal(result.values, expected)
"""


def test_indicator_ATR():
    n = 3
    result = ATR(df, n)
    isinstance(result, pd.DataFrame)
    expected = talib.ATR(df['High'].values, df['Low'].values, df['Close'].values, timeperiod=n)
    np.testing.assert_almost_equal(result.values, expected)

"""
def test_indicator_BBANDS():
    n = 3
    result = BBANDS(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_PPSR():
    result = PPSR(df)
    isinstance(result, pd.DataFrame)

def test_indicator_STOK():
    result = STOK(df)
    isinstance(result, pd.DataFrame)

def test_indicator_STO():
    n = 2
    result = STO(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_TRIX():
    n = 3
    result = TRIX(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_ADX():
    (n, n_ADX) = (2, 4)
    result = ADX(df, n, n_ADX)
    isinstance(result, pd.DataFrame)

def test_indicator_MACD():
    (n_fast, n_slow) = (9, 13)
    result = MACD(df, n_fast, n_slow)
    isinstance(result, pd.DataFrame)

def test_indicator_MassI():
    result = MassI(df)
    isinstance(result, pd.DataFrame)

def test_indicator_Vortex():
    n = 2
    result = Vortex(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_KST():
    (r1, r2, r3, r4, n1, n2, n3, n4) = (1, 2, 3, 4, 6, 7, 9, 9)
    result = KST(df, r1, r2, r3, r4, n1, n2, n3, n4)
    isinstance(result, pd.DataFrame)

def test_indicator_RSI():
    n = 2
    result = RSI(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_TSI():
    (r, s) = (2, 4)
    result = TSI(df, r, s)
    isinstance(result, pd.DataFrame)

def test_indicator_ACCDIST():
    n = 2
    result = ACCDIST(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_Chaikin():
    result = Chaikin(df)
    isinstance(result, pd.DataFrame)

def test_indicator_MFI():
    n = 2
    result = MFI(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_OBV():
    n = 2
    result = OBV(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_FORCE():
    n = 2
    result = FORCE(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_EOM():
    n = 2
    result = EOM(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_CCI():
    n = 2
    result = CCI(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_COPP():
    n = 2
    result = COPP(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_COPP():
    n = 2
    result = COPP(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_KELCH():
    n = 2
    result = KELCH(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_ULTOSC():
    n = 2
    result = ULTOSC(df)
    isinstance(result, pd.DataFrame)

def test_indicator_DONCH():
    n = 2
    result = DONCH(df, n)
    isinstance(result, pd.DataFrame)

def test_indicator_STDDEV():
    n = 2
    result = STDDEV(df, n)
    isinstance(result, pd.DataFrame)
"""
