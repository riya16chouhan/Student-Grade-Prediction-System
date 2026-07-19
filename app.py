import streamlit as st
import joblib
import numpy as np

# Load Model and Scaler
model = joblib.load("gaussian.pkl")
scaler = joblib.load("scaler_.pkl")

# Page Configuration
st.set_page_config(
    page_title="Student Grade Prediction System",
    page_icon="🎓",
    layout="centered"
)

# Title
st.title("🎓 Student Grade Prediction System")
st.markdown("### Predict Student Grade Class using Machine Learning")
st.write("---")

# Input Fields
age = st.number_input("Age", min_value=10, max_value=30, value=18)

gender = st.selectbox("Gender", ["Male", "Female"])
ethnicity = st.selectbox("Ethnicity", [0, 1, 2, 3])
parent_edu = st.selectbox("Parental Education", [0, 1, 2, 3, 4])

study_time = st.slider("Weekly Study Time (Hours)", 0.0, 40.0, 10.0)
absences = st.number_input("Absences", 0, 50, 5)
gpa = st.slider("GPA", 0.0, 4.0, 3.0, 0.1)

tutoring = st.selectbox("Tutoring", ["No", "Yes"])
parent_support = st.selectbox("Parental Support", [0, 1, 2, 3, 4])
extra = st.selectbox("Extracurricular Activities", ["No", "Yes"])
sports = st.selectbox("Sports", ["No", "Yes"])
music = st.selectbox("Music", ["No", "Yes"])
volunteer = st.selectbox("Volunteering", ["No", "Yes"])

# Convert Yes/No to 0/1
gender = 1 if gender == "Male" else 0
tutoring = 1 if tutoring == "Yes" else 0
extra = 1 if extra == "Yes" else 0
sports = 1 if sports == "Yes" else 0
music = 1 if music == "Yes" else 0
volunteer = 1 if volunteer == "Yes" else 0

# Prediction Button
if st.button("Predict Grade"):

    data = np.array([[
        age,
        gender,
        ethnicity,
        parent_edu,
        study_time,
        absences,
        tutoring,
        parent_support,
        extra,
        sports,
        music,
        volunteer,
        gpa
    ]])

    data = scaler.transform(data)
    prediction = model.predict(data)

    grade = int(prediction[0])

    st.success(f"🎯 Predicted Grade Class: {grade}")

    if grade == 0:
        st.info("Excellent Performance ⭐")
    elif grade == 1:
        st.info("Very Good Performance 👍")
    elif grade == 2:
        st.info("Good Performance 🙂")
    elif grade == 3:
        st.warning("Average Performance")
    else:
        st.error("Needs Improvement 📚")