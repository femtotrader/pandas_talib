#!/usr/bin/env python
# -*- coding: utf-8 -*-

# $ pip install pandas_datareader

from pandas_datareader import data, wb

def main():
    df = data.DataReader("GOOG", 'yahoo', "2014-01-01", "2014-12-31")

    print(df)


    panel = data.DataReader(["AAPL", "GOOGL", "IBM"], 'yahoo', "2014-01-01", "2014-12-31")

    print(panel)


if __name__ == '__main__':
    main()