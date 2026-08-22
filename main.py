import streamlit as st
from prediction_helper import predict

st.set_page_config(
    page_title="Insurance Premium Prediction",
    page_icon="💰",
    layout="wide"
)

st.title("Insurance Premium Prediction")
st.write("Enter the customer details below.")


# -----------------------------
# Row 1
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=0,
        max_value=100,
        value=30
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col3:
    region = st.selectbox(
        "Region",
        ["Northwest", "Southeast", "Northeast", "Southwest"]
    )


# -----------------------------
# Row 2
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    marital_status = st.selectbox(
        "Marital Status",
        ["Unmarried", "Married"]
    )

with col2:
    number_of_dependants = st.number_input(
        "Number of Dependants",
        min_value=0,
        max_value=20,
        value=0
    )

with col3:
    bmi_category = st.selectbox(
        "BMI Category",
        ["Normal", "Obesity", "Overweight", "Underweight"]
    )


# -----------------------------
# Row 3
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    smoking_status = st.selectbox(
        "Smoking Status",
        ["No Smoking", "Regular", "Occasional"]
    )

with col2:
    employment_status = st.selectbox(
        "Employment Status",
        ["Salaried", "Self-Employed", "Freelancer"]
    )

with col3:
    income_lakhs = st.number_input(
        "Income (Lakhs)",
        min_value=0.0,
        value=5.0,
        step=0.1
    )


# -----------------------------
# Row 4
# -----------------------------
col1, col2, col3 = st.columns(3)

with col1:
    medical_history = st.selectbox(
        "Medical History",
        [
            "Diabetes",
            "High blood pressure",
            "No Disease",
            "Diabetes & High blood pressure",
            "Thyroid",
            "Heart disease",
            "High blood pressure & Heart disease",
            "Diabetes & Thyroid",
            "Diabetes & Heart disease"
        ]
    )

with col2:
    insurance_plan = st.selectbox(
        "Insurance Plan",
        ["Bronze", "Silver", "Gold"]
    )

with col3:
    genetical_risk = st.number_input(
        "Genetical Risk",
        min_value=0,
        max_value=10,
        value=0
    )


# -----------------------------
# Predict Button
# -----------------------------
st.divider()

col1, col2, col3 = st.columns([1, 1, 1])

with col1:
    predict_clicked = st.button("Predict")

if predict_clicked:

    insurance_plan_mapping = {
        "Bronze": 1,
        "Silver": 2,
        "Gold": 3
    }

    input_dict = {
        "age": age,
        "gender": gender,
        "region": region,
        "marital_status": marital_status,
        "number_of_dependants": number_of_dependants,
        "bmi_category": bmi_category,
        "smoking_status": smoking_status,
        "employment_status": employment_status,
        "income_lakhs": income_lakhs,
        "medical_history": medical_history,
        "insurance_plan": insurance_plan_mapping[insurance_plan],
        "genetical_risk": genetical_risk
    }

    prediction = predict(input_dict)

    st.success(f"Predicted Insurance Premium: {prediction}")