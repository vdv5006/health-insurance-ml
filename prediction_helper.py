import pandas as pd
from joblib import load

model_rest = load("artifacts/model_rest.joblib")
model_young = load("artifacts/model_young.joblib")
scaler_rest = load("artifacts/scaler_rest.joblib")
scaler_young = load("artifacts/scaler_young.joblib")

def predict(input_dict):
    df = pd.DataFrame(
        0,
        columns=[
            'age',
            'number_of_dependants',
            'income_lakhs',
            'insurance_plan',
            'total_risk_score',
            'genetical_risk',

            'gender_Male',

            'region_Northwest',
            'region_Southeast',
            'region_Southwest',

            'marital_status_Unmarried',

            'bmi_category_Obesity',
            'bmi_category_Overweight',
            'bmi_category_Underweight',

            'smoking_status_Occasional',
            'smoking_status_Regular',

            'employment_status_Salaried',
            'employment_status_Self-Employed'
        ],
        index=[0]
    )

    # --------------------------------------------------
    # Numeric columns
    # --------------------------------------------------

    df["age"] = input_dict["age"]

    df["number_of_dependants"] = input_dict[
        "number_of_dependants"
    ]

    df["income_lakhs"] = input_dict["income_lakhs"]

    df["insurance_plan"] = input_dict["insurance_plan"]

    df["genetical_risk"] = input_dict["genetical_risk"]

    # --------------------------------------------------
    # Gender
    #
    # Male     -> gender_Male = 1
    # Female   -> gender_Male = 0
    # --------------------------------------------------

    if input_dict["gender"] == "Male":
        df["gender_Male"] = 1

    # --------------------------------------------------
    # Region
    #
    # Northeast is the reference category
    # because there is no region_Northeast column.
    # --------------------------------------------------

    if input_dict["region"] == "Northwest":
        df["region_Northwest"] = 1

    elif input_dict["region"] == "Southeast":
        df["region_Southeast"] = 1

    elif input_dict["region"] == "Southwest":
        df["region_Southwest"] = 1

    # --------------------------------------------------
    # Marital Status
    #
    # Married is the reference category
    # --------------------------------------------------

    if input_dict["marital_status"] == "Unmarried":
        df["marital_status_Unmarried"] = 1

    # --------------------------------------------------
    # BMI Category
    #
    # Normal is the reference category
    # --------------------------------------------------

    if input_dict["bmi_category"] == "Obesity":
        df["bmi_category_Obesity"] = 1

    elif input_dict["bmi_category"] == "Overweight":
        df["bmi_category_Overweight"] = 1

    elif input_dict["bmi_category"] == "Underweight":
        df["bmi_category_Underweight"] = 1

    # --------------------------------------------------
    # Smoking Status
    #
    # No Smoking is the reference category
    # --------------------------------------------------

    if input_dict["smoking_status"] == "Occasional":
        df["smoking_status_Occasional"] = 1

    elif input_dict["smoking_status"] == "Regular":
        df["smoking_status_Regular"] = 1

    # --------------------------------------------------
    # Employment Status
    #
    # Freelancer is the reference category
    # --------------------------------------------------

    if input_dict["employment_status"] == "Salaried":
        df["employment_status_Salaried"] = 1

    elif input_dict["employment_status"] == "Self-Employed":
        df["employment_status_Self-Employed"] = 1

    # --------------------------------------------------
    # Medical History
    #
    # Calculate total_risk_score
    # --------------------------------------------------

    medical_history = input_dict["medical_history"]

    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }

    # Split multiple diseases using "&"
    diseases = medical_history.split("&")

    # Clean and convert to lowercase
    diseases = [
        disease.lower().strip()
        for disease in diseases
    ]

    # Calculate total risk score
    total_risk_score = sum(
        risk_scores.get(disease, 0)
        for disease in diseases
    )

    df["total_risk_score"] = total_risk_score

    # --------------------------------------------------
    # Select model/scaler
    # --------------------------------------------------

    # Example:
    # Young customers -> young model
    # Others -> rest model

    if input_dict["age"] <= 25:

        cols_to_scale = scaler_young["cols_to_scale"]
        scaler = scaler_young["scaler"]

        df[cols_to_scale] = scaler.transform(df[cols_to_scale])

        df = df[model_young.feature_names_in_]

        prediction = model_young.predict(df)

    else:

        cols_to_scale = scaler_rest["cols_to_scale"]
        scaler = scaler_rest["scaler"]

        df[cols_to_scale] = scaler.transform(df[cols_to_scale])

        df = df[model_rest.feature_names_in_]

        prediction = model_rest.predict(df)

    return int(prediction)




