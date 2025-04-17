import yfinance as yf
import pandas as pd
import numpy as np
import os

# Function to fetch stock data (static method for simplicity)
def fetch_stock_data(ticker, start_date, end_date):
    # Using Yahoo Finance API (yfinance) to fetch historical data
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    return stock_data

# Function to simulate predictions with noise
def get_mock_predictions(df):
    # Copy the original dataframe to avoid modifying it directly
    prediction = df.copy()

    # Ensure random noise matches the length of the 'Close' column
    random_noise = 0.01 * np.random.randn(len(prediction))  # Noise for each row in the DataFrame
    
    # Apply the noise to 'Close' to create predictions
    prediction['Predicted'] = prediction['Close'] * (1 + random_noise)  # Apply the noise
    
    return prediction

# Function to load stock list (static example)
def load_stock_list():
    # Static stock list as example (you could replace this with your actual data)
    stock_list = [
        {'ticker': 'AAPL', 'name': 'Apple Inc.'},
        {'ticker': 'GOOGL', 'name': 'Alphabet Inc.'},
        {'ticker': 'AMZN', 'name': 'Amazon.com Inc.'},
        {'ticker': 'MSFT', 'name': 'Microsoft Corp.'},
        {'ticker': 'TSLA', 'name': 'Tesla Inc.'},
    ]
    
    # Returning as a pandas DataFrame
    return pd.DataFrame(stock_list)

# Sample function to save stock data as CSV (for use with static data)
def save_stock_data(df, ticker):
    filename = f"stock_data_{ticker}.csv"
    df.to_csv(filename, index=False)

# Example of loading saved stock data from CSV
def load_saved_stock_data(ticker):
    filename = f"stock_data_{ticker}.csv"
    if os.path.exists(filename):
        return pd.read_csv(filename)
    else:
        print(f"Data for {ticker} not found, downloading fresh data.")
        return None
