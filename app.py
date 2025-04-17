import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from data_fetch import get_cached_stock_list, fetch_stock_data, get_mock_predictions, get_news_and_earnings

st.set_page_config(page_title="📈 Stock Prediction AI", layout="wide")
st.title("📈 Stock Prediction AI")

# Layout columns
col1, col2 = st.columns([3, 1])

# Choose exchange
exchange = st.selectbox("Select Exchange", ["NSE", "BSE"])

# Load static stock list
stock_list = get_cached_stock_list(exchange)
selected_stock = st.selectbox("🔍 Choose a Stock", stock_list)

# Main chart area
with col1:
    if selected_stock:
        df = fetch_stock_data(selected_stock, exchange)
        prediction = get_mock_predictions(df)

        st.subheader(f"📊 Historical + Predicted Prices for {selected_stock} ({exchange})")

        fig, ax = plt.subplots(figsize=(10, 4))
        ax.plot(df.index, df['Close'], label="Actual", linewidth=2)
        ax.plot(prediction.index, prediction['Predicted'], label="Prediction", linestyle='--')
        ax.set_xlabel("Date")
        ax.set_ylabel("Price (₹)")
        ax.legend()
        st.pyplot(fig)

        st.markdown("### 📄 Raw Data")
        st.dataframe(df.tail())

# News + Earnings Panel
with col2:
    st.markdown("### 📰 News & Earnings")
    news_data = get_news_and_earnings(selected_stock)

    if news_data:
        for item in news_data.get("news", []):
            color = "green" if item["impact"] == "positive" else ("red" if item["impact"] == "negative" else "gray")
            st.markdown(f"<div style='padding:8px; border-left: 4px solid {color}; margin-bottom: 10px;'>"
                        f"<strong>{item['date']}</strong><br>{item['title']}"
                        f"</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("### 📊 Earnings")
        for quarter, report in news_data.get("earnings", {}).items():
            st.markdown(f"**{quarter}:** {report}")
    else:
        st.info("No news/earnings data available for this stock.")
