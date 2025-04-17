from nsepython import nse_eq
import pandas as pd
import os
import json
import yfinance as yf

def get_nse_stock_list():
    # Fetch stocks in NIFTY 100
    df = nse_eq("NIFTY 100")  # You can change this to NIFTY 50, 500 etc.
    stock_list = [item['symbol'] for item in df['data']]
    return sorted(stock_list)

def get_cached_stock_list(filepath="nse_stock_list.json"):
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            return json.load(f)
    else:
        stock_list = get_nse_stock_list()
        with open(filepath, "w") as f:
            json.dump(stock_list, f)
        return stock_list

def fetch_stock_data(symbol, period="6mo", interval="1d"):
    symbol_yf = symbol + ".NS"  # Add NSE suffix for yfinance
    df = yf.download(symbol_yf, period=period, interval=interval)
    return df
