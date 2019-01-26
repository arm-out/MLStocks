import numpy as np
import pandas as pd
import pickle

def process_for_labels(ticker):
    days = 7
    df = pd.read_csv('sp500_joined_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, days+1):
        df['{}_{}'.format(ticker, i)] = (df[ticker].shift(-i) - df[ticker]) / df[ticker]

    df.fillna(0, inplace=True)
    return tickers, df

def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1
        if col < -requiremen:
            return -1
    return 0

def extract_featuresets(ticker):
    ticker, df = process_for_labels(ticker)
    #df['{}_target'.format(ticker)] = list(map(buy_sell_hold,))
