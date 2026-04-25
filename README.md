# ⚡ Electricity Demand Forecasting

## 📌 About the Project
This project is about predicting future electricity demand using time series analysis.

The main idea was to understand how electricity consumption changes over time and build a model that can forecast future demand. This can be useful for energy planning, avoiding shortages, and managing resources efficiently.

---

## 🎯 What I Did
I worked on the complete flow of a real-world data project:

- Cleaned and prepared time-based data  
- Explored trends and seasonal patterns  
- Built forecasting models  
- Compared their performance  
- Deployed the final model using Streamlit  

---

## 📊 Understanding the Data
The dataset contains historical electricity consumption values over time.

Since this is time series data, each value depends on previous values. While exploring, I noticed:
- A clear upward trend  
- Repeating seasonal patterns  

---

## 🔍 Key Steps in the Project

### 1. Data Preparation
- Converted date column into proper datetime format  
- Set it as index for time-based analysis  

---

### 2. Checking Stationarity
Time series models like ARIMA require stationary data.

- I used the ADF test  
- Found that the data was non-stationary  
- Applied differencing to fix it  

---

### 3. Model Building

I built two models:

- **ETS Model** → Handles trend & seasonality  
- **SARIMA Model** → Captures both mathematically  

I used `auto_arima` to find the best parameters automatically.

---

### 4. Model Comparison

To evaluate performance, I used:
- RMSE  
- MAPE  
- RMSPE  

👉 SARIMA performed better because it captured the patterns more accurately.

---

### 5. Forecasting
Using the final SARIMA model, I predicted electricity demand for the next 24 months.

The forecast successfully showed both:
- Trend  
- Seasonal variation  

---

## 🌐 Deployment
I deployed the project using Streamlit to make it interactive.

### App Features:
- User can select number of months to forecast  
- Displays predicted values  
- Shows a visualization graph  
- Provides summary insights  

---

## ⚠️ Note
The model file is not uploaded to GitHub because of size limitations.  
It is handled separately during deployment.

---

## 💡 What I Learned
- How to work with time series data  
- Importance of stationarity  
- Difference between ETS and SARIMA  
- How to deploy ML models using Streamlit  

---

## 🚀 Future Improvements
- Add external factors like weather  
- Try advanced models like LSTM  
- Improve UI of the app  

---

## 👩‍💻 Author
Vaishali Mehta  






