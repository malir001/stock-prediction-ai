import streamlit as st
from data_fetch import get_cached_stock_list, fetch_stock_data

st.set_page_config(page_title="Stock Prediction AI", layout="centered")
st.title("📈 Stock Prediction AI")

# Cache the stock list to avoid re-fetching
@st.cache_data
def load_stock_list():
    return get_cached_stock_list()

# Get stock list and show dropdown
stock_list = load_stock_list()
selected_stock = st.selectbox("🔍 Choose a Stock", stock_list)

# Fetch and show data
if selected_stock:
    st.subheader(f"Stock History: {selected_stock}")
    df = fetch_stock_data(selected_stock)

    if df is not None and not df.empty:
        st.line_chart(df['Close'])
        st.write(df.tail())
    else:
        st.warning("No data available. Try another stock.")
