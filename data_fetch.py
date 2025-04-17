import yfinance as yf
import pandas as pd
import json
import os
import numpy as np  # Ensure numpy is imported

# Function to get cached stock list (static stock list for testing)
def get_cached_stock_list(exchange):
    # Sample stock list for NSE and BSE
    if exchange == "NSE":
        return ["RELIANCE.NS", "TCS.NS", "INFY.NS", "HDFC.NS", "ITC.NS"]
    elif exchange == "BSE":
        return ["500325.BO", "500180.BO", "500410.BO", "532500.BO", "500209.BO"]
    else:
        return []

# Function to fetch stock data using Yahoo Finance (via yfinance)
def fetch_stock_data(ticker, exchange):
    # Fetch historical stock data (1 year of daily data)
    data = yf.download(ticker, period="1y", interval="1d")
    return data

# Mock prediction data (you can replace with your ML model or any other method)
def get_mock_predictions(df):
    # Generate a dummy prediction by shifting the closing price
    prediction = df.copy()
    # Ensure np.random.randn matches the length of 'Close' column
    random_noise = 0.01 * np.random.randn(len(prediction))  # Generate random noise
    # Convert random_noise to a pandas Series to align it properly with 'Close' column
    prediction['Predicted'] = prediction['Close'] * (1 + pd.Series(random_noise, index=prediction.index))  # Apply the noise to Close
    return prediction

# Mock function to get news and earnings
def get_news_and_earnings(stock):
    # Static mock news and earnings data
    news_data = {
        "news": [
            {
                "date": "2025-04-18",
                "title": "Reliance Industries announces strong quarterly results",
                "impact": "positive"
            },
            {
                "date": "2025-04-10",
                "title": "Political tensions in India impact stock market",
                "impact": "negative"
            }
        ],
        "earnings": {
            "Q1 2025": "EPS: ₹10.5, Revenue: ₹50,000 Crore",
            "Q4 2024": "EPS: ₹8.7, Revenue: ₹45,000 Crore"
        }
    }
    return news_data
