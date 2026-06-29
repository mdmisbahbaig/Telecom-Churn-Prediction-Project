# Telco Customer Churn Prediction

## About the Project

This project aims to predict whether a telecom customer is likely to leave the company (churn) based on customer information, services used, contract details, and billing information.

The main goal of this project is to help telecom companies identify customers who are at risk of churning so that they can take action to retain them.

---

## Problem Statement

Customer churn is a major challenge for telecom companies because losing customers leads to revenue loss. The objective of this project is to build a machine learning model that can predict customer churn and help improve customer retention.

---

## Business Objective

The business objective of this project is to identify customers who are likely to churn and understand the factors that influence customer churn.

---

## Dataset Information

The dataset contains information about customers, including:

* Customer demographics
* Services subscribed
* Contract details
* Payment methods
* Billing information
* Customer churn status

### Target Variable

**Churn Value**

* 0 = Customer stayed
* 1 = Customer churned

---

## Exploratory Data Analysis (EDA)

The following analyses were performed:

* Univariate Analysis
* Bivariate Analysis
* Customer behavior analysis
* Churn pattern analysis
* Business insights extraction

---

## Data Preprocessing

The following preprocessing techniques were used:

* Handling missing values
* Binary encoding
* Ordinal encoding
* One-hot encoding
* Feature scaling
* ColumnTransformer

---

## Machine Learning Models Used

The following models were trained and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* Gradient Boosting
* XGBoost

---

## Final Model Selection

After comparing multiple models, **Logistic Regression** was selected as the final model because it provided performance similar to more complex models while being easier to interpret and explain.

### Final Model Performance

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 81.24% |
| Precision | 70.03% |
| Recall    | 57.97% |
| F1 Score  | 63.43% |

---

## Key Business Insights

* Customers with longer tenure are less likely to churn.
* Customers with long-term contracts have lower churn rates.
* Customers using fiber optic internet have a higher chance of churning.
* Customers with online security and tech support services are less likely to churn.
* Customers with dependents are less likely to leave the company.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Streamlit

---

## Project Files

```text
Telco-Customer-Churn-Prediction/

├── EDA.ipynb
├── Model_Training.ipynb
├── app.py
├── model.pkl
├── preprocessor.pkl
├── requirements.txt
└── README.md
```

---

## Streamlit Application

This project includes an interactive Streamlit application where users can enter customer details and predict:

* Customer churn prediction
* Churn probability
* Risk level
* Key factors influencing the prediction

---

## Future Improvements

* Improve model performance using advanced tuning techniques.
* Add explainable AI methods such as SHAP.
* Deploy the application on cloud platforms.
