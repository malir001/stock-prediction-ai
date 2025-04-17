
import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

def fetch_stock_data(ticker, period="2y"):
    stock = yf.Ticker(ticker)
    hist = stock.history(period=period)
    return hist

def fetch_earnings(ticker):
    stock = yf.Ticker(ticker)
    try:
        return stock.earnings
    except:
        return pd.DataFrame()
