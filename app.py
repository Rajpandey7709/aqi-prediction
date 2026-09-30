import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("aqi_model.pkl", "rb") as file:
    model = pickle.load(file)

# App title
st.set_page_config(page_title="AQI Predictor", page_icon="🌫️")
st.title("🌫️ Air Quality Index (AQI) Prediction App")

st.write("Enter pollutant values to predict AQI")

# Input fields
pm25 = st.number_input("PM2.5", min_value=0.0, step=1.0)
pm10 = st.number_input("PM10", min_value=0.0, step=1.0)
no2 = st.number_input("NO2", min_value=0.0, step=1.0)

# Predict button
if st.button("Predict AQI"):
    input_data = np.array([[pm25, pm10, no2]])
    prediction = model.predict(input_data)

    aqi_value = round(prediction[0], 2)

    st.success(f"Predicted AQI: {aqi_value}")

    # AQI category
    if aqi_value <= 50:
        st.info("Air Quality: Good 😊")
    elif aqi_value <= 100:
        st.info("Air Quality: Satisfactory 🙂")
    elif aqi_value <= 200:
        st.warning("Air Quality: Moderate 😷")
    elif aqi_value <= 300:
        st.warning("Air Quality: Poor 🤒")
    else:
        st.error("Air Quality: Very Poor / Severe ☠️")
