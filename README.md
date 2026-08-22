
# Insurance Premium Prediction

A machine learning project that predicts a customer's insurance premium based on demographic, financial, lifestyle, and medical information.

The project includes a **Streamlit web application** where users can enter customer details and get an estimated insurance premium.

## Features

The application takes the following customer information as input:

* Age
* Gender
* Region
* Marital Status
* Number of Dependants
* BMI Category
* Smoking Status
* Employment Status
* Income
* Medical History
* Insurance Plan
* Genetical Risk

Based on these inputs, the application predicts the expected insurance premium.

## Machine Learning Approach

The prediction pipeline uses different models based on the customer's age:

* **Age ≤ 25:** Young customer model
* **Age > 25:** Rest-of-customers model

Separate scalers are also used for the two customer groups.

The prediction process includes:

1. Accepting customer information through the Streamlit UI.
2. Converting categorical variables into numerical features using one-hot encoding logic.
3. Calculating a `total_risk_score` from the customer's medical history.
4. Selecting the appropriate model based on age.
5. Scaling the required numerical features.
6. Making the insurance premium prediction.

## Medical Risk Score

Medical conditions are assigned risk scores:

| Medical Condition   | Risk Score |
| ------------------- | ---------: |
| No Disease          |          0 |
| Thyroid             |          5 |
| Diabetes            |          6 |
| High Blood Pressure |          6 |
| Heart Disease       |          8 |

For customers with multiple medical conditions, the individual risk scores are added together to calculate the `total_risk_score`.

For example:

```text
Diabetes & Heart disease
= 6 + 8
= 14
```

## Project Structure

```text
insurance-premium-prediction/
│
├── app.py
├── prediction_helper.py
├── artifacts/
│   ├── model_rest.joblib
│   ├── model_young.joblib
│   ├── scaler_rest.joblib
│   └── scaler_young.joblib
│
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* Scikit-learn
* Joblib
* Streamlit
* Machine Learning

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd insurance-premium-prediction
```

Create and activate a virtual environment:

```bash
python -m venv venv
```

On Windows:

```bash
venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Run the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

## Prediction Workflow

```text
Customer Input
      ↓
Feature Engineering
      ↓
Calculate Medical Risk Score
      ↓
Select Model Based on Age
      ↓
Scale Required Features
      ↓
ML Model Prediction
      ↓
Predicted Insurance Premium
```

## Example

A user can enter customer information such as:

```text
Age: 30
Gender: Male
Region: Northwest
Marital Status: Married
Dependants: 2
BMI Category: Normal
Smoking Status: No Smoking
Employment Status: Salaried
Income: 8 Lakhs
Medical History: No Disease
Insurance Plan: 2
Genetical Risk: 1
```

The application processes these inputs and displays the predicted insurance premium.

## Disclaimer

This project is intended for **educational and demonstration purposes only**. The predicted premium should not be considered an actual insurance quote or financial advice.

