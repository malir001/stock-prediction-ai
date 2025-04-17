import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_fetch import get_cached_stock_list, fetch_stock_data, get_mock_predictions, get_news_and_earnings

# Set page configuration for a wider layout
st.set_page_config(layout="wide")

# Select stock from cached list (static data)
exchange = st.selectbox('Select Stock Exchange', ['NSE', 'BSE'])
stocks = get_cached_stock_list(exchange)
stock_symbol = st.selectbox('Select Stock', stocks)

# Fetch stock data from Yahoo Finance
df = fetch_stock_data(stock_symbol, exchange)

# Display the raw data
st.write(f"Displaying data for: {stock_symbol}")
st.dataframe(df)

# Get predictions based on mock data
prediction = get_mock_predictions(df)

# Plotting stock price and predicted prices
st.subheader(f"Stock Price vs Predicted Price for {stock_symbol}")
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(df.index, df['Close'], label='Close Price', color='blue')
ax.plot(prediction.index, prediction['Predicted'], label='Predicted Price', linestyle='--', color='red')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title(f'{stock_symbol} Stock Price Prediction')
ax.legend()
st.pyplot(fig)

# Fetch mock news and earnings for the stock
news_data = get_news_and_earnings(stock_symbol)

# Display news in a side panel
with st.sidebar:
    st.subheader("News & Earnings")
    st.write("### Latest News")
    for news in news_data['news']:
        st.write(f"**{news['date']}**: {news['title']} ({news['impact']})")

    st.write("### Earnings Reports")
    for quarter, earnings in news_data['earnings'].items():
        st.write(f"**{quarter}**: {earnings}")

