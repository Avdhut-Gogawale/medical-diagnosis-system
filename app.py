import streamlit as st
import pickle
import numpy as np

# Load the diabetes model and scaler
diabetes_model = pickle.load(open("diabetes_model.pkl", "rb"))
diabetes_scaler = pickle.load(open("diabetes_scaler.pkl", "rb"))

# Load the heart disease model and scaler
heart_model = pickle.load(open("heart_disease_model.pkl", "rb"))
heart_scaler = pickle.load(open("heart_scaler.pkl", "rb"))

# Page title
st.title("AI-Powered Medical Diagnosis System")

# Sidebar for disease selection
disease_option = st.sidebar.selectbox("Select Disease to Predict", ("Diabetes", "Heart Disease"))

def predict_diabetes():
    st.header("Diabetes Prediction")

    # Input fields
    pregnancies = st.number_input("Pregnancies", min_value=0)
    glucose = st.number_input("Glucose Level", min_value=0)
    blood_pressure = st.number_input("Blood Pressure", min_value=0)
    skin_thickness = st.number_input("Skin Thickness", min_value=0)
    insulin = st.number_input("Insulin Level", min_value=0)
    bmi = st.number_input("BMI", min_value=0.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0)
    age = st.number_input("Age", min_value=0)

    if st.button("Predict Diabetes"):
        # Prepare input
        user_input = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
        user_input_scaled = diabetes_scaler.transform(user_input)

        # Make prediction
        prediction = diabetes_model.predict(user_input_scaled)
        
        # Output
        if prediction[0] == 1:
            st.error("The model predicts that the patient is likely to have diabetes.")
        else:
            st.success("The model predicts that the patient is unlikely to have diabetes.")

def predict_heart_disease():
    st.header("Heart Disease Prediction")

    # Input fields
    age = st.number_input("Age", min_value=0)
    sex = st.selectbox("Sex (1 = Male, 0 = Female)", [0, 1])
    cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3)
    trestbps = st.number_input("Resting Blood Pressure", min_value=0)
    chol = st.number_input("Cholesterol Level", min_value=0)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)", [0, 1])
    restecg = st.number_input("Resting ECG (0-2)", min_value=0, max_value=2)
    thalach = st.number_input("Max Heart Rate Achieved", min_value=0)
    exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [0, 1])
    oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0)
    slope = st.number_input("Slope of Peak Exercise ST Segment (0-2)", min_value=0, max_value=2)
    ca = st.number_input("Number of Major Vessels (0-4)", min_value=0, max_value=4)
    thal = st.number_input("Thalassemia (0-3)", min_value=0, max_value=3)

    if st.button("Predict Heart Disease"):
        # Prepare input
        user_input = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        user_input_scaled = heart_scaler.transform(user_input)

        # Make prediction
        prediction = heart_model.predict(user_input_scaled)

        # Output
        if prediction[0] == 1:
            st.error("The patient is likely to have heart disease.")
        else:
            st.success("The patient is unlikely to have heart disease.")

# Display the correct prediction page
if disease_option == "Diabetes":
    predict_diabetes()
else:
    predict_heart_disease()
