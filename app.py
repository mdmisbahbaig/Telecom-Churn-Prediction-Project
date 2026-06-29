import numpy as np
import pandas as pd
import streamlit as st
import pickle

# Loading model
model = pickle.load(open('model.pkl', 'rb'))

# Loading preprocessor
preprocessor = pickle.load(open('preprocessor.pkl', 'rb'))

# Loading threshold
with open('threshold.pkl', 'rb') as f:
    threshold = pickle.load(f)


st.set_page_config(page_title = 'Telecom Churn Prediction using ML', layout="wide")

st.title("Customer Churn Prediction System")

with st.sidebar:

    st.title("📊 Project Overview")

    st.markdown("""
    **Project:** Telecom Customer Churn Prediction system

    **Objective:**
    Predict customers who are likely to leave the telecom company.

    **Problem Type:**
    Binary Classification
                
    **Tools Used in Project:**
    - Python
    - Numpy
    - Pandas
    - Matplotlib
    - Seaborn
    - Scikit-Learn
    - XGBoost
    - Streamlit
    - GitHub

    **Model Performance:**
    - Accuracy: **81.24%**
    - Precision: **70.03%**
    - Recall: **57.97%**
    - F1 Score: **63.43%**

    **Key Factors Affecting Churn:**
    - Contract Type
    - Tenure Months
    - Internet Service
    - Online Security
    - Tech Support
    
    **Developed By:**            
    Md Misbah Baig""")

col1, col2 = st.columns(2, gap = 'large')

with col1:
    st.subheader('👤 Customer Information')
    gender = st.selectbox("Gender", ['Male', 'Female'])

    senior_citizen = st.selectbox("Senior Citizen", ['Yes', 'No'])

    partner = st.selectbox("Partner", ['Yes', 'No'])

    dependents = st.selectbox("Dependents", ['Yes', 'No'])


    st.subheader('💳 Billing Information')

    paperless_billing = st.selectbox("Paperless Billing", ['Yes', 'No'])

    payment_method = st.selectbox( 'Payment Method', ['Mailed check', 'Electronic check', 'Bank transfer (automatic)', 'Credit card (automatic)'])

    multiple_lines = st.selectbox("Mulitple Lines", ['No', 'Yes', 'No phone service'])

    tenure_months = st.slider("Tenure Months", 0, 100)

    monthly_charges = st.slider("Monthly Charges",0.0,150.0,50.0)

    

with col2:

    st.subheader('🌐 Internet & Services')

    internet_service = st.selectbox("Internet Service", ['DSL', 'Fiber optic', 'No'])

    online_security = st.selectbox("Online Security", ['Yes', 'No', 'No internet service'])

    online_backup = st.selectbox("Online Backup", ['Yes', 'No', 'No internet service'])

    device_protection = st.selectbox("Device Protection", ['No', 'Yes', 'No internet service'])

    tech_support = st.selectbox("Tech Support", ['No', 'Yes', 'No internet service'])

    streaming_tv = st.selectbox('Streaming TV', ['No', 'Yes', 'No internet service'])

    streaming_movies = st.selectbox('Streaming Movies', ['No', 'Yes', 'No internet service'])

    st.subheader('📞 Phone Services')

    contract = st.selectbox("Contract", ['Month-to-month', 'Two year', 'One year'])

    phone_service = st.selectbox("Phone Service", ['Yes', 'No'])

X_input = pd.DataFrame([[gender, senior_citizen, partner, dependents, tenure_months,
                          phone_service, multiple_lines, internet_service, online_security,
                            online_backup, device_protection, tech_support, streaming_tv,
                              streaming_movies, contract, paperless_billing, payment_method, 
                              monthly_charges, monthly_charges * tenure_months]],
    
                           columns= ['Gender', 'Senior Citizen', 'Partner', 'Dependents', 'Tenure Months',
       'Phone Service', 'Multiple Lines', 'Internet Service',
       'Online Security', 'Online Backup', 'Device Protection', 'Tech Support',
       'Streaming TV', 'Streaming Movies', 'Contract', 'Paperless Billing',
       'Payment Method', 'Monthly Charges', 'Total Charges'])

X_trf = preprocessor.transform(X_input)

if st.button("Predict"):
    st.success("✅Predicted churn successfully.")
    # pred = model.predict(X_trf)
    probability = model.predict_proba(X_trf)[0][1]
    if probability >= threshold:
        prediction = 1
    else:
        prediction = 0

    col21, col22 = st.columns(2)

    with col21:
        st.subheader('Prediction')
        if prediction == 1:
            st.text('⚠️ Customer is likely to churn')
        else:
            st.text("✅ Customer is not likely to churn")
        
        pred_prob = round((model.predict_proba(X_trf)[0,1] * 100), 2)
        st.write("Churn Probability:", pred_prob,'%')
        
        if pred_prob > 0 and pred_prob <= 30:
            st.write("Risk Level: Low Risk")
        elif pred_prob > 30 and pred_prob <=70:
            st.write("Risk Level: Medium Risk")
        else:
            st.write("Risk Level: ⚠️ High Risk")

    with col22:

        if prediction == 1:
            st.subheader("Key Factors Increasing Churn Risk")

            factors = []

            if contract == 'Month-to-month':
                factors.append("• Customer has a month-to-month contract")

            if internet_service == 'Fiber optic':
                factors.append("• Customer uses fiber optic internet service")

            if paperless_billing == 'Yes':
                factors.append("• Customer uses paperless billing")

            if payment_method == 'Electronic check':
                factors.append("• Customer uses electronic check payment")

            if tenure_months < 12:
                factors.append("• Customer tenure is low")

            if tech_support == 'No':
                factors.append("• Customer does not have tech support")

            if online_security == 'No':
                factors.append("• Customer does not have online security")

            if len(factors) == 0:
                st.write("• No major churn risk factors identified")

            for factor in factors:
                st.write(factor)

        else:
            st.subheader("📊 Factors Reducing Churn Risk")

            factors = []

            if contract in ['One year', 'Two year']:
                factors.append("• Customer has a long-term contract")

            if tenure_months >= 24:
                factors.append("• Customer has long tenure with the company")

            if tech_support == 'Yes':
                factors.append("• Customer has subscribed to tech support")

            if online_security == 'Yes':
                factors.append("• Customer has subscribed to online security")

            if dependents == 'Yes':
                factors.append("• Customer has dependents")

            if payment_method == 'Credit card (automatic)':
                factors.append("• Customer uses automatic payment")

            if len(factors) == 0:
                st.write("• No major retention factors identified")

            for factor in factors:
                st.write(factor)