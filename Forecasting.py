import streamlit as st
import pickle
import pandas as pd
import numpy as np
import os

# Page config
st.set_page_config(page_title="Electricity Demand Forecasting", layout="wide")

# Title
st.title("⚡ Electricity Demand Forecasting Dashboard")

# Sidebar
st.sidebar.header("User Input")

# Load model
@st.cache_resource


def load_model():
    if not os.path.exists("model.pkl"):
        url = "https://drive.google.com/uc?export=download&id=1Ud8k5z-mmUjE1CmhWGh4Q1E2QEfb-sTM"
        gdown.download(url, "model.pkl", quiet=False)
    
    return pickle.load(open("model.pkl", "rb"))

model = load_model()

# Input: forecast horizon
steps = st.sidebar.slider("Select number of months to forecast", 1, 60, 24)

# Generate forecast
forecast = model.predict(n_periods=steps)

# Create date range for forecast
last_date = pd.to_datetime("2019-12-01")  # last date from your dataset
future_dates = pd.date_range(start=last_date, periods=steps+1, freq='MS')[1:]

forecast_df = pd.DataFrame({
    "Date": future_dates,
    "Forecasted_Demand": forecast
})

forecast_df.set_index("Date", inplace=True)

# Layout
col1, col2 = st.columns(2)

# Show data
with col1:
    st.subheader("📊 Forecasted Values")
    st.dataframe(forecast_df)

# Metrics
with col2:
    st.subheader("📈 Summary Stats")
    st.metric("Max Demand", f"{np.max(forecast):.2f}")
    st.metric("Min Demand", f"{np.min(forecast):.2f}")
    st.metric("Average Demand", f"{np.mean(forecast):.2f}")

# Plot
st.subheader("📉 Forecast Visualization")
st.line_chart(forecast_df)

# Download option
st.subheader("⬇️ Download Forecast Data")
csv = forecast_df.to_csv().encode('utf-8')
st.download_button(
    label="Download CSV",
    data=csv,
    file_name='forecast.csv',
    mime='text/csv'
)

# Footer
st.markdown("---")
st.markdown("Time Series Forecasting (SARIMA)")