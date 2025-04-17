import yfinance as yf

# Use static NSE stock symbols for now
def get_cached_stock_list():
    return [
        "RELIANCE", "TCS", "INFY", "HDFCBANK", "ICICIBANK", "SBIN",
        "HINDUNILVR", "ITC", "KOTAKBANK", "LT", "BAJFINANCE", "AXISBANK"
    ]

def fetch_stock_data(symbol, period="6mo", interval="1d"):
    symbol_yf = symbol + ".NS"  # Add NSE suffix for yfinance
    df = yf.download(symbol_yf, period=period, interval=interval)
    return df
