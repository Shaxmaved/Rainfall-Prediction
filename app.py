import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load("model.pkl")

st.title("🌧️ Rainfall Prediction using Decision Tree")
st.write("Enter weather parameters to predict whether it will rain or not.")

# Input fields
pressure = st.number_input("Pressure (hPa)", min_value=800.0, max_value=1100.0, value=1013.0)
dewpoint = st.number_input("Dew Point (°C)", min_value=-20.0, max_value=40.0, value=12.0)
humidity = st.slider("Humidity (%)", 0, 100, 70)
cloud = st.slider("Cloud Cover (%)", 0, 100, 50)
sunshine = st.number_input("Sunshine (hours)", min_value=0.0, max_value=12.0, value=6.0)
winddirection = st.slider("Wind Direction (°)", 0, 360, 180)
windspeed = st.number_input("Wind Speed (km/h)", min_value=0.0, max_value=100.0, value=10.0)

# Prediction
if st.button("Predict Rainfall"):
    input_data = np.array([[pressure, dewpoint, humidity, cloud, sunshine, winddirection, windspeed]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("🌧️ Prediction: It will rain.")
    else:
        st.info("☀️ Prediction: No rain expected.")
    
