#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ pip install pandas_datareader

import os
from pandas_datareader import data, wb
import datetime
import pytz

def main():
    basepath = os.path.dirname(__file__)

    year = 2014
    tzinfo = pytz.UTC
    dt_from = datetime.datetime(year, 1, 1, tzinfo=tzinfo)
    dt_to = datetime.datetime(year, 12, 1, tzinfo=tzinfo)

    symbol = "GOOG"
    df = data.DataReader(symbol, 'yahoo', dt_from, dt_to)
    fmt_dt = "%Y%m%d"
    print(df)

    filename = os.path.join(basepath, "%s_%s_%s.p" % (symbol, dt_from.strftime(fmt_dt), dt_to.strftime(fmt_dt)))
    print("Output: %s" % filename)
    df.to_pickle(filename)

    filename = os.path.join(basepath, "%s_%s_%s.csv" % (symbol, dt_from.strftime(fmt_dt), dt_to.strftime(fmt_dt)))
    print("Output: %s" % filename)
    df.to_csv(filename)

    symbols = ["AAPL", "GOOGL", "IBM"]
    print(filename)

    panel = data.DataReader(symbols, 'yahoo', dt_from, dt_to)
    print(panel)
    #print(panel.loc['Open','2014-02-03','AAPL'])
    filename = os.path.join(basepath, "%s_%s_%s.p" % ("_".join(symbols), dt_from.strftime(fmt_dt), dt_to.strftime(fmt_dt)))
    print("Output: %s" % filename)
    panel.to_pickle(filename)
    filename = os.path.join(basepath, "%s_%s_%s.xls" % ("_".join(symbols), dt_from.strftime(fmt_dt), dt_to.strftime(fmt_dt)))
    print("Output: %s" % filename)
    panel.to_excel(filename)
    for symbol in symbols:
        filename = os.path.join(basepath, "%s_%s_%s.csv" % (symbol, dt_from.strftime(fmt_dt), dt_to.strftime(fmt_dt)))
        print("Output: %s" % filename)
        df = panel.loc[:, :, symbol]
        df.to_csv(filename)


    #panel.to_json(filename)
    #panel.to_csv(filename)

if __name__ == '__main__':
    main()