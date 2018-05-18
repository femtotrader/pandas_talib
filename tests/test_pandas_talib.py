#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import unittest

import pandas as pd
import numpy as np
import talib
from pandas_talib import *

basepath = os.path.dirname(__file__)
filename = os.path.join(basepath, "..", "data", "AAPL_GOOGL_IBM_20140101_20141201.xls")
d = pd.read_excel(filename, sheetname=None)
panel = pd.Panel.from_dict(d)
panel = panel.iloc[:, 1:, :]
panel.major_axis.name = "Date"

df = panel.loc[:, :, 'AAPL']

SETTINGS.join = False


class TestFunctions(unittest.TestCase):

    def test_indicator_SMA(self):
        timeperiod = 10
        random_serie = pd.DataFrame(np.random.uniform(0, 1, size=10), columns=['last'])
        result = SMA(random_serie, timeperiod, key='last')
        isinstance(result, pd.DataFrame)
        expected = talib.SMA(random_serie['last'].values, timeperiod=10)
        np.testing.assert_almost_equal(result.values, expected)

    def test_indicator_MA(self):
        n = 3
        price = 'Close'
        result = MA(df, n)
        isinstance(result, pd.DataFrame)
        expected = talib.MA(df[price].values, timeperiod=n)
        np.testing.assert_almost_equal(result.values, expected)

    def test_indicator_EMA(self):
        n = 3
        price = 'Close'
        result = EMA(df, n)
        isinstance(result, pd.DataFrame)
        expected = talib.EMA(df[price].values, timeperiod=n)
        np.testing.assert_almost_equal(result.values, expected)

    def test_indicator_MOM(self):
        n = 3
        price = 'Close'
        result = MOM(df, n)
        isinstance(result, pd.DataFrame)
        expected = talib.MOM(df[price].values, timeperiod=n)
        np.testing.assert_almost_equal(result.values, expected)

    def test_indicator_ROC(self):
        n = 3
        price = 'Close'
        result = ROC(df, n)
        isinstance(result, pd.DataFrame)
        expected = talib.ROC(df[price].values, timeperiod=n)
        np.testing.assert_almost_equal(result.values, expected)

    def test_indicator_ATR(self):
        n = 5
        result = ATR(df, n)
        isinstance(result, pd.DataFrame)
        
        expected = talib.ATR(df['High'].values, df['Low'].values, df['Close'].values, timeperiod=n)
        
        np.testing.assert_almost_equal(result, expected[1::])

    def test_indicator_BBANDS(self):
        n = 3
        result = BBANDS(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_PPSR(self):
        result = PPSR(df)
        isinstance(result, pd.DataFrame)

    def test_indicator_STOK(self):
        result = STOK(df)
        isinstance(result, pd.DataFrame)

    def test_indicator_STO(self):
        n = 2
        result = STO(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_TRIX(self):
        n = 3
        result = TRIX(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_ADX(self):
        (n, n_ADX) = (2, 4)
        result = ADX(df, n, n_ADX)
        isinstance(result, pd.DataFrame)

    def test_indicator_MACD(self):
        (n_fast, n_slow) = (9, 13)
        result = MACD(df, n_fast, n_slow)
        isinstance(result, pd.DataFrame)

    def test_indicator_MassI(self):
        result = MassI(df)
        isinstance(result, pd.DataFrame)

    def test_indicator_Vortex(self):
        n = 2
        result = Vortex(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_KST(self):
        (r1, r2, r3, r4, n1, n2, n3, n4) = (1, 2, 3, 4, 6, 7, 9, 9)
        result = KST(df, r1, r2, r3, r4, n1, n2, n3, n4)
        isinstance(result, pd.DataFrame)

    def test_indicator_RSI(self):
        n = 2
        result = RSI(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_TSI(self):
        (r, s) = (2, 4)
        result = TSI(df, r, s)
        isinstance(result, pd.DataFrame)

    def test_indicator_ACCDIST(self):
        n = 2
        result = ACCDIST(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_Chaikin(self):
        result = Chaikin(df)
        isinstance(result, pd.DataFrame)

    def test_indicator_MFI(self):
        n = 2
        result = MFI(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_OBV(self):
        n = 2
        result = OBV(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_FORCE(self):
        n = 2
        result = FORCE(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_EOM(self):
        n = 2
        result = EOM(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_CCI(self):
        n = 2
        result = CCI(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_COPP(self):
        n = 2
        result = COPP(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_COPP(self):
        n = 2
        result = COPP(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_KELCH(self):
        n = 2
        result = KELCH(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_ULTOSC(self):
        n = 2
        result = ULTOSC(df)
        isinstance(result, pd.DataFrame)

    def test_indicator_DONCH(self):
        n = 2
        result = DONCH(df, n)
        isinstance(result, pd.DataFrame)

    def test_indicator_STDDEV(self):
        n = 2
        result = STDDEV(df, n)
        isinstance(result, pd.DataFrame)
