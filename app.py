
import streamlit as st
from data_fetch import fetch_stock_data
from model import prepare_data, build_model
from sentiment import analyze_sentiment
import matplotlib.pyplot as plt
import numpy as np

st.title("📈 AI-Based Stock Forecasting")

ticker = st.text_input("Enter Stock Ticker (e.g., AAPL)", "AAPL")
data = fetch_stock_data(ticker)
st.write("Recent Data:", data.tail())

X, y, scaler = prepare_data(data)
model = build_model((X.shape[1], 1))
model.fit(X, y, epochs=5, batch_size=32, verbose=0)

predicted = model.predict(X)
predicted_prices = scaler.inverse_transform(predicted)

st.subheader("📊 Actual vs Predicted Closing Prices")
fig, ax = plt.subplots()
ax.plot(data['Close'][60:].values, label='Actual')
ax.plot(predicted_prices, label='Predicted')
ax.legend()
st.pyplot(fig)

st.subheader("📰 News Sentiment Analysis (Sample)")
news_sample = "Company revenue rose sharply in the last quarter beating expectations"
sentiment = analyze_sentiment(news_sample)
st.write("Sentiment Score:", sentiment)
