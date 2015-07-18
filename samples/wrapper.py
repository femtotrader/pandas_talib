#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
import talib
from talib import SMA
#from talib.abstract import SMA

def main():
    basepath = os.path.dirname(__file__)
    filename = os.path.join(basepath, "..", "data", "AAPL_GOOGL_IBM_20140101_20141201.xls")
    d = pd.read_excel(filename, sheetname=None)
    panel = pd.Panel.from_dict(d)
    #print(panel.loc['Open','2014-02-03','AAPL'])
    panel = panel.iloc[:,1:,:]
    panel.major_axis.name = "Date"
    #print(panel)

    df = panel.loc[:,:,'AAPL']
    #print(df)

    result = SMA(df['Close'].values, timeperiod=4) # Function API
    #result = SMA(df, timeperiod=4, price='Close') # Abstract API
    print(result)

if __name__ == '__main__':
    main()
