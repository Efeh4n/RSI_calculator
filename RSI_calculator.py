from numpy.ma.core import negative
from statsmodels.regression.rolling import RollingOLS
import pandas_datareader as web
import matplotlib.pyplot as plt
import statsmodels.api as sm
import pandas as pd
import numpy as np
import datetime as dt
import yfinance as yf
import warnings
def settings() :
    warnings.filterwarnings('ignore')
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', 100)
    pd.set_option('display.width', None)
settings()
ticker = 'AAPL'
end_date = '2024-09-27'
start_date = pd.to_datetime(end_date) - pd.DateOffset(365)
data = yf.download(ticker, start=start_date, end=end_date)
delta = data['Adj Close'].diff(1)
delta.dropna(inplace=True)
positive = delta.copy()
negative = delta.copy()
positive[positive < 0] = 0
negative[negative > 0] = 0
days = 14
average_gain = positive.rolling(window=days).mean()
average_loss = abs(negative.rolling(window=days).mean())
ralative_strength = average_gain / average_loss
RSI = 100.0 - (100.0 / (1 + ralative_strength))
data['RSI'] = RSI
print(data)