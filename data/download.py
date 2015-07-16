#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ pip install pandas_datareader

from pandas_datareader import data, wb
import datetime
import pytz

def main():
    year = 2014
    tzinfo = pytz.UTC
    dt_from = datetime.datetime(year, 1, 1, tzinfo=tzinfo)
    dt_to = datetime.datetime(year, 12, 1, tzinfo=tzinfo)

    symbol = "GOOG"
    #df = data.DataReader(symbol, 'yahoo', dt_from, dt_to)
    fmt_dt = "%Y%m%d"
    filename = "%s_%s_%s.csv" % (symbol, dt_from.strftime(fmt_dt), dt_to.strftime(fmt_dt))
    print(filename)
    #print(df)
    #df.to_csv(filename)


    symbols = ["AAPL", "GOOGL", "IBM"]
    filename = "%s_%s_%s.csv" % ("_".join(symbols), dt_from.strftime(fmt_dt), dt_to.strftime(fmt_dt))
    print(filename)

    #panel = data.DataReader(symbols, 'yahoo', dt_from, dt_to)
    #print(panel)
    #df.to_csv(filename)

if __name__ == '__main__':
    main()