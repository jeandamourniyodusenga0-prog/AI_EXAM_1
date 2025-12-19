import streamlit as st
import pickle
import numpy as np
import os

# Path to the saved model using your registration number
model_path = '25RP19438_model.pkl'

st.title("🌱 Crop Yield Predictor")

# Check if the model file exists
if os.path.exists(model_path):
    # Load the saved Linear Regression model
    model = pickle.load(open(model_path, 'rb'))

    # User input for temperature
    temp = st.number_input(
        "Enter Average Temperature (°C):", 
        min_value=0.0, 
        max_value=100.0, 
        value=25.0
    )

    # Predict button
    if st.button("Predict Crop Yield"):
        prediction = model.predict(np.array([[temp]]))
        st.success(f"Predicted Crop Yield: {prediction[0]:.2f} kg/ha")

else:
    st.error(
        f"Model file '{model_path}' not found. "
        "Please run the training script first to save the model."
    )