import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("diabetes_logistic_model.pkl")

st.title("Diabetes Prediction App")
st.write("Enter the patient information to predict the diabetes outcome.")

Pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
Glucose = st.number_input("Glucose", min_value=0.0, value=120.0)
BloodPressure = st.number_input("Blood Pressure", min_value=0.0, value=70.0)
SkinThickness = st.number_input("Skin Thickness", min_value=0.0, value=20.0)
Insulin = st.number_input("Insulin", min_value=0.0, value=80.0)
BMI = st.number_input("BMI", min_value=0.0, value=30.0)
DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function", min_value=0.0, value=0.5)
Age = st.number_input("Age", min_value=1, max_value=120, value=30)

# Prediction block
if st.button("Predict"):

    data = pd.DataFrame({
        "Pregnancies": [Pregnancies],
        "Glucose": [Glucose],
        "BloodPressure": [BloodPressure],
        "SkinThickness": [SkinThickness],
        "Insulin": [Insulin],
        "BMI": [BMI],
        "DiabetesPedigreeFunction": [DiabetesPedigreeFunction],
        "Age": [Age]
    })

    prediction = model.predict(data)[0]

    if prediction == 0:
        st.success(" No Diabetes Predicted")
    else:
        st.error("Diabetes Predicted")

