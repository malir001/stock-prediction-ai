import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Static stock list (NSE/BSE)
def get_cached_stock_list(exchange):
    if exchange == "NSE":
        return ["RELIANCE", "TCS", "INFY", "HDFCBANK"]
    else:
        return ["RELIANCE.BSE", "TCS.BSE", "INFY.BSE", "HDFCBANK.BSE"]

# Static stock data (mocked)
def fetch_stock_data(symbol, exchange):
    dates = pd.date_range(end=datetime.today(), periods=100)
    prices = np.cumsum(np.random.randn(100)) + 200
    df = pd.DataFrame({"Date": dates, "Close": prices})
    df.set_index("Date", inplace=True)
    return df

# Fake prediction after last 15 days
def get_mock_predictions(df):
    last_date = df.index[-1]
    future_dates = [last_date + timedelta(days=i) for i in range(1, 16)]
    last_price = df['Close'].iloc[-1]
    trend = np.linspace(0, 5, 15)
    noise = np.random.randn(15)
    pred_prices = last_price + trend + noise
    pred_df = pd.DataFrame({"Predicted": pred_prices}, index=future_dates)
    return pred_df

# Static news + earnings
news_db = {
    "RELIANCE": {
        "news": [
            {"title": "Reliance Q4 profit up 12%, beats analyst expectations", "date": "2024-04-21", "impact": "positive"},
            {"title": "Middle East tensions raise global oil prices; RIL stock reacts", "date": "2024-01-15", "impact": "negative"}
        ],
        "earnings": {
            "Q3": "₹16,200 Cr profit, 8.2% YoY growth",
            "Q4": "₹18,000 Cr profit, 12% YoY growth"
        }
    },
    "TCS": {
        "news": [
            {"title": "TCS wins $1.5B contract from UK Govt", "date": "2024-03-05", "impact": "positive"},
            {"title": "IT sector slowdown weighs on TCS revenue", "date": "2024-02-12", "impact": "negative"}
        ],
        "earnings": {
            "Q3": "₹10,800 Cr profit, 5% YoY growth",
            "Q4": "₹11,500 Cr profit, 7% YoY growth"
        }
    }
}

# Provide news/earnings for selected stock
def get_news_and_earnings(symbol):
    key = symbol.replace(".BSE", "")
    return news_db.get(key, {})
