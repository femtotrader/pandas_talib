#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pandas as pd
from pandas_talib import *

def main():
    basepath = os.path.dirname(__file__)
    filename = os.path.join(basepath, "..", "data", "AAPL_GOOGL_IBM_20140101_20141201.xls")
    d = pd.read_excel(filename, sheetname=None)
    panel = pd.Panel.from_dict(d)
    #print(panel.loc['Open','2014-02-03','AAPL'])
    panel = panel.iloc[:,1:,:]
    panel.major_axis.name = "Date"
    #print(panel)

    df_AAPL = panel.loc[:,:,'AAPL']
    print(df_AAPL)

    SETTINGS.join = False
    print(MA(df_AAPL, 3))

if __name__ == '__main__':
    main()
