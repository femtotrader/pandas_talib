'''
Created on April 15, 2012

@author: Bruno Franca
'''
import numpy
from pandas import *
from math import *

#Moving Average
def MA(df, n):
    MA = Series(rolling_mean(df['Close'], n), name = 'MA_' + str(n))
    df = df.join(MA)
    return df

#Exponential Moving Average
def EMA(df, n):
    EMA = Series(ewma(df['Close'], span = n, min_periods = n - 1), name = 'EMA_' + str(n))
    df = df.join(EMA)
    return df

#Momentum
def MOM(df, n):
    M = Series(df['Close'].diff(n), name = 'Momentum_' + str(n))
    df = df.join(M)
    return df

#Rate of Change
def ROC(df, n):
    M = df['Close'].diff(n - 1)
    N = df['Close'].shift(n - 1)
    ROC = Series(M / N, name = 'ROC_' + str(n))
    df = df.join(ROC)
    return df

#Average True Range
def ATR(df, n):
    i = 0
    TR_l = [0]
    while i < df.index[-1]:
        TR = max(df.get_value(i + 1, 'High'), df.get_value(i, 'Close')) - min(df.get_value(i + 1, 'Low'), df.get_value(i, 'Close'))
        TR_l.append(TR)
        i = i + 1
    TR_s = Series(TR_l)
    ATR = Series(ewma(TR_s, span = n, min_periods = n), name = 'ATR_' + str(n))
    df = df.join(ATR)
    return df

#Bollinger Bands
def BBANDS(df, n):
    MA = Series(rolling_mean(df['Close'], n))
    MSD = Series(rolling_std(df['Close'], n))
    b1 = 4 * MSD / MA
    B1 = Series(b1, name = 'BollingerB_' + str(n))
    df = df.join(B1)
    b2 = (df['Close'] - MA + 2 * MSD) / (4 * MSD)
    B2 = Series(b2, name = 'Bollinger%b_' + str(n))
    df = df.join(B2)
    return df

#Pivot Points, Supports and Resistances
def PPSR(df):
    PP = Series((df['High'] + df['Low'] + df['Close']) / 3)
    R1 = Series(2 * PP - df['Low'])
    S1 = Series(2 * PP - df['High'])
    R2 = Series(PP + df['High'] - df['Low'])
    S2 = Series(PP - df['High'] + df['Low'])
    R3 = Series(df['High'] + 2 * (PP - df['Low']))
    S3 = Series(df['Low'] - 2 * (df['High'] - PP))
    psr = {'PP':PP, 'R1':R1, 'S1':S1, 'R2':R2, 'S2':S2, 'R3':R3, 'S3':S3}
    PSR = DataFrame(psr)
    df = df.join(PSR)
    return df

#Stochastic oscillator %K
def STOK(df):
    SOk = Series((df['Close'] - df['Low']) / (df['High'] - df['Low']), name = 'SO%k')
    df = df.join(SOk)
    return df

#Stochastic oscillator %D
def STO(df, n):
    SOk = Series((df['Close'] - df['Low']) / (df['High'] - df['Low']), name = 'SO%k')
    SOd = Series(ewma(SOk, span = n, min_periods = n - 1), name = 'SO%d_' + str(n))
    df = df.join(SOd)
    return df

#Trix
def TRIX(df, n):
    EX1 = ewma(df['Close'], span = n, min_periods = n - 1)
    EX2 = ewma(EX1, span = n, min_periods = n - 1)
    EX3 = ewma(EX2, span = n, min_periods = n - 1)
    i = 0
    ROC_l = [0]
    while i + 1 <= df.index[-1]:
        ROC = (EX3[i + 1] - EX3[i]) / EX3[i]
        ROC_l.append(ROC)
        i = i + 1
    Trix = Series(ROC_l, name = 'Trix_' + str(n))
    df = df.join(Trix)
    return df

#Average Directional Movement Index
def ADX(df, n, n_ADX):
    i = 0
    UpI = []
    DoI = []
    while i + 1 <= df.index[-1]:
        UpMove = df.get_value(i + 1, 'High') - df.get_value(i, 'High')
        DoMove = df.get_value(i, 'Low') - df.get_value(i + 1, 'Low')
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else: UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else: DoD = 0
        DoI.append(DoD)
        i = i + 1
    i = 0
    TR_l = [0]
    while i < df.index[-1]:
        TR = max(df.get_value(i + 1, 'High'), df.get_value(i, 'Close')) - min(df.get_value(i + 1, 'Low'), df.get_value(i, 'Close'))
        TR_l.append(TR)
        i = i + 1
    TR_s = Series(TR_l)
    ATR = Series(ewma(TR_s, span = n, min_periods = n))
    UpI = Series(UpI)
    DoI = Series(DoI)
    PosDI = Series(ewma(UpI, span = n, min_periods = n - 1) / ATR)
    NegDI = Series(ewma(DoI, span = n, min_periods = n - 1) / ATR)
    ADX = Series(ewma(abs(PosDI - NegDI) / (PosDI + NegDI), span = n_ADX, min_periods = n_ADX - 1), name = 'ADX_' + str(n) + '_' + str(n_ADX))
    df = df.join(ADX)
    return df

#MACD, MACD Signal and MACD difference
def MACD(df, n_fast, n_slow):
    EMAfast = Series(ewma(df['Close'], span = n_fast, min_periods = n_slow - 1))
    EMAslow = Series(ewma(df['Close'], span = n_slow, min_periods = n_slow - 1))
    MACD = Series(EMAfast - EMAslow, name = 'MACD_' + str(n_fast) + '_' + str(n_slow))
    MACDsign = Series(ewma(MACD, span = 9, min_periods = 8), name = 'MACDsign_' + str(n_fast) + '_' + str(n_slow))
    MACDdiff = Series(MACD - MACDsign, name = 'MACDdiff_' + str(n_fast) + '_' + str(n_slow))
    df = df.join(MACD)
    df = df.join(MACDsign)
    df = df.join(MACDdiff)
    return df

#Mass Index
def MassI(df):
    Range = df['High'] - df['Low']
    EX1 = ewma(Range, span = 9, min_periods = 8)
    EX2 = ewma(EX1, span = 9, min_periods = 8)
    Mass = EX1 / EX2
    MassI = Series(rolling_sum(Mass, 25), name = 'Mass Index')
    df = df.join(MassI)
    return df

#Vortex Indicator
def Vortex(df, n):
    i = 0
    TR = [0]
    while i < df.index[-1]:
        Range = max(df.get_value(i + 1, 'High'), df.get_value(i, 'Close')) - min(df.get_value(i + 1, 'Low'), df.get_value(i, 'Close'))
        TR.append(Range)
        i = i + 1
    i = 0
    VM = [0]
    while i < df.index[-1]:
        Range = abs(df.get_value(i + 1, 'High') - df.get_value(i, 'Low')) - abs(df.get_value(i + 1, 'Low') - df.get_value(i, 'High'))
        VM.append(Range)
        i = i + 1
    VI = Series(rolling_sum(Series(VM), n) / rolling_sum(Series(TR), n), name = 'Vortex_' + str(n))
    df = df.join(VI)
    return df

#KST Oscillator
def KST(df, r1, r2, r3, r4, n1, n2, n3, n4):
    M = df['Close'].diff(r1 - 1)
    N = df['Close'].shift(r1 - 1)
    ROC1 = M / N
    M = df['Close'].diff(r2 - 1)
    N = df['Close'].shift(r2 - 1)
    ROC2 = M / N
    M = df['Close'].diff(r3 - 1)
    N = df['Close'].shift(r3 - 1)
    ROC3 = M / N
    M = df['Close'].diff(r4 - 1)
    N = df['Close'].shift(r4 - 1)
    ROC4 = M / N
    KST = Series(rolling_sum(ROC1, n1) + rolling_sum(ROC2, n2) * 2 + rolling_sum(ROC3, n3) * 3 + rolling_sum(ROC4, n4) * 4, name = 'KST_' + str(r1) + '_' + str(r2) + '_' + str(r3) + '_' + str(r4) + '_' + str(n1) + '_' + str(n2) + '_' + str(n3) + '_' + str(n4))
    df = df.join(KST)
    return df

#Relative Strength Index
def RSI(df, n):
    i = 0
    UpI = [0]
    DoI = [0]
    while i + 1 <= df.index[-1]:
        UpMove = df.get_value(i + 1, 'High') - df.get_value(i, 'High')
        DoMove = df.get_value(i, 'Low') - df.get_value(i + 1, 'Low')
        if UpMove > DoMove and UpMove > 0:
            UpD = UpMove
        else: UpD = 0
        UpI.append(UpD)
        if DoMove > UpMove and DoMove > 0:
            DoD = DoMove
        else: DoD = 0
        DoI.append(DoD)
        i = i + 1
    UpI = Series(UpI)
    DoI = Series(DoI)
    PosDI = Series(ewma(UpI, span = n, min_periods = n - 1))
    NegDI = Series(ewma(DoI, span = n, min_periods = n - 1))
    RSI = Series(PosDI / (PosDI + NegDI), name = 'RSI_' + str(n))
    df = df.join(RSI)
    return df

#True Strength Index
def TSI(df, r, s):
    M = Series(df['Close'].diff(1))
    aM = abs(M)
    EMA1 = Series(ewma(M, span = r, min_periods = r - 1))
    aEMA1 = Series(ewma(aM, span = r, min_periods = r - 1))
    EMA2 = Series(ewma(EMA1, span = s, min_periods = s - 1))
    aEMA2 = Series(ewma(aEMA1, span = s, min_periods = s - 1))
    TSI = Series(EMA2 / aEMA2, name = 'TSI_' + str(r) + '_' + str(s))
    df = df.join(TSI)
    return df

#Accumulation/Distribution
def ACCDIST(df, n):
    ad = (2 * df['Close'] - df['High'] - df['Low']) / (df['High'] - df['Low']) * df['Volume']
    M = ad.diff(n - 1)
    N = ad.shift(n - 1)
    ROC = M / N
    AD = Series(ROC, name = 'Acc/Dist_ROC_' + str(n))
    df = df.join(AD)
    return df

#Chaikin Oscillator
def Chaikin(df):
    ad = (2 * df['Close'] - df['High'] - df['Low']) / (df['High'] - df['Low']) * df['Volume']
    Chaikin = Series(ewma(ad, span = 3, min_periods = 2) - ewma(ad, span = 10, min_periods = 9), name = 'Chaikin')
    df = df.join(Chaikin)
    return df

#Money Flow Index and Ratio
def MFI(df, n):
    PP = (df['High'] + df['Low'] + df['Close']) / 3
    i = 0
    PosMF = [0]
    while i < df.index[-1]:
        if PP[i + 1] > PP[i]:
            PosMF.append(PP[i + 1] * df.get_value(i + 1, 'Volume'))
        else:
            PosMF.append(0)
        i = i + 1
    PosMF = Series(PosMF)
    TotMF = PP * df['Volume']
    MFR = Series(PosMF / TotMF)
    MFI = Series(rolling_mean(MFR, n), name = 'MFI_' + str(n))
    df = df.join(MFI)
    return df

#On-balance Volume
def OBV(df, n):
    i = 0
    OBV = [0]
    while i < df.index[-1]:
        if df.get_value(i + 1, 'Close') - df.get_value(i, 'Close') > 0:
            OBV.append(df.get_value(i + 1, 'Volume'))
        if df.get_value(i + 1, 'Close') - df.get_value(i, 'Close') == 0:
            OBV.append(0)
        if df.get_value(i + 1, 'Close') - df.get_value(i, 'Close') < 0:
            OBV.append(-df.get_value(i + 1, 'Volume'))
        i = i + 1
    OBV = Series(OBV)
    OBV_ma = Series(rolling_mean(OBV, n), name = 'OBV_' + str(n))
    df = df.join(OBV_ma)
    return df

#Force Index
def FORCE(df, n):
    F = Series(df['Close'].diff(n) * df['Volume'].diff(n), name = 'Force_' + str(n))
    df = df.join(F)
    return df

#Ease of Movement
def EOM(df, n):
    EoM = (df['High'].diff(1) + df['Low'].diff(1)) * (df['High'] - df['Low']) / (2 * df['Volume'])
    Eom_ma = Series(rolling_mean(EoM, n), name = 'EoM_' + str(n))
    df = df.join(Eom_ma)
    return df

#Commodity Channel Index
def CCI(df, n):
    PP = (df['High'] + df['Low'] + df['Close']) / 3
    CCI = Series((PP - rolling_mean(PP, n)) / rolling_std(PP, n), name = 'CCI_' + str(n))
    df = df.join(CCI)
    return df

#Coppock Curve
def COPP(df, n):
    M = df['Close'].diff(int(n * 11 / 10) - 1)
    N = df['Close'].shift(int(n * 11 / 10) - 1)
    ROC1 = M / N
    M = df['Close'].diff(int(n * 14 / 10) - 1)
    N = df['Close'].shift(int(n * 14 / 10) - 1)
    ROC2 = M / N
    Copp = Series(ewma(ROC1 + ROC2, span = n, min_periods = n), name = 'Copp_' + str(n))
    df = df.join(Copp)
    return df

#Keltner Channel
def KELCH(df, n):
    KelChM = Series(rolling_mean((df['High'] + df['Low'] + df['Close']) / 3, n), name = 'KelChM_' + str(n))
    KelChU = Series(rolling_mean((4 * df['High'] - 2 * df['Low'] + df['Close']) / 3, n), name = 'KelChU_' + str(n))
    KelChD = Series(rolling_mean((-2 * df['High'] + 4 * df['Low'] + df['Close']) / 3, n), name = 'KelChD_' + str(n))
    df = df.join(KelChM)
    df = df.join(KelChU)
    df = df.join(KelChD)
    return df

#Ultimate Oscillator
def ULTOSC(df):
    i = 0
    TR_l = [0]
    BP_l = [0]
    while i < df.index[-1]:
        TR = max(df.get_value(i + 1, 'High'), df.get_value(i, 'Close')) - min(df.get_value(i + 1, 'Low'), df.get_value(i, 'Close'))
        TR_l.append(TR)
        BP = df.get_value(i + 1, 'Close') - min(df.get_value(i + 1, 'Low'), df.get_value(i, 'Close'))
        BP_l.append(BP)
        i = i + 1
    UltO = Series((4 * rolling_sum(Series(BP_l), 7) / rolling_sum(Series(TR_l), 7)) + (2 * rolling_sum(Series(BP_l), 14) / rolling_sum(Series(TR_l), 14)) + (rolling_sum(Series(BP_l), 28) / rolling_sum(Series(TR_l), 28)), name = 'Ultimate_Osc')
    df = df.join(UltO)
    return df

#Donchian Channel
def DONCH(df, n):
    i = 0
    DC_l = []
    while i < n - 1:
        DC_l.append(0)
        i = i + 1
    i = 0
    while i + n - 1 < df.index[-1]:
        DC = max(df['High'].ix[i:i + n - 1]) - min(df['Low'].ix[i:i + n - 1])
        DC_l.append(DC)
        i = i + 1
    DonCh = Series(DC_l, name = 'Donchian_' + str(n))
    DonCh = DonCh.shift(n - 1)
    df = df.join(DonCh)
    return df

#Standard Deviation
def STDDEV(df, n):
    df = df.join(Series(rolling_std(df['Close'], n), name = 'STD_' + str(n)))
    return df
