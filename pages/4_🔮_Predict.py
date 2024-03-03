import streamlit as st
import pandas as pd
import numpy as np
import joblib  
import pyodbc
import os as os
from sklearn.preprocessing import LabelEncoder
from catboost import CatBoostClassifier
from imblearn.over_sampling import RandomOverSampler
from sklearn.linear_model import LogisticRegression
from  PIL import Image

st.set_page_config(
    page_icon= "🔮",
    page_title= "Predict",
    layout = "wide"
    )

st.title(f"**Predict Customer Churn ➡️**")
st.write(
    """
    Keep your customers happy!  This app helps you predict customer churn using machine learning, empowering you to take proactive steps and prevent revenue loss.
    """
     )
#image
chun_img = Image.open(
    os.path.join (
        os.getcwd(),
        "assets/images/chun customer image 2.png"
        )
    )

#display img
st.image(
    chun_img,
    use_column_width=True,
    caption= " Customers leaving can sting your business. Predict & prevent churn!"
    )

#  session state
if 'final_prediction' not in st.session_state:
    st.session_state.final_prediction = None

# Load models and cache them
@st.cache(allow_output_mutation=True)
def load_catboost():
    Catboost = joblib.load('models/catboost_pipeline.joblib')
    return Catboost

@st.cache(allow_output_mutation=True)
def load_logistic():
    Logistic = joblib.load('models/logistic_pipeline.joblib')
    return Logistic

# Create a form for user input
def user_input_form():
    with st.form(key='user_input_form', clear_on_submit=True):
        st.header('**User Input**⚪')
        tenure = st.number_input(label='tenure')
        SeniorCitizen = st.radio(label='SeniorCitizen', options=[1,2])
        gender = st.selectbox(label='Gender', options=['Male', 'Female'])
        Partner = st.selectbox(label='Partner', options=['Yes', 'No'])
        Dependents = st.selectbox(label='Dependents', options=['Yes', 'No'])
        st.header('**Services**🔴')
        PhoneService = st.selectbox(label='PhoneService', options=['Yes', 'No'])
        MultipleLines = st.selectbox(label='MultipleLines', options=['Yes', 'No'])
        InternetService = st.selectbox(label='InternetService', options=['DSL', 'Fiber Optic', 'No'])
        OnlineSecurity = st.selectbox(label='OnlineSecurity', options=['Yes', 'No', 'No Internet'])
        OnlineBackup = st.selectbox(label='OnlineBackup', options=['Yes', 'No', 'No Internet'])
        DeviceProtection = st.selectbox(label='DeviceProtection', options=['Yes', 'No', 'No Internet'])
        TechSupport = st.selectbox(label='TechSupport', options=['Yes', 'No', 'No Internet'])
        StreamingTV = st.selectbox(label='StreamingTV', options=['Yes', 'No', 'No Internet'])
        StreamingMovies = st.selectbox(label='StreamingMovies', options=['Yes', 'No', 'No Internet'])
        st.header('**Payment**⚫')
        contract = st.selectbox(label='contract', options=['Month-to-Month', 'One year', 'Two year'])
        PaperlessBilling = st.selectbox(label='PaperlessBilling', options=['Yes', 'No'])
        PaymentMethod = st.selectbox(label='PaymentMethod', options=['Electronic check', 'mailed check', 'Bank transfer(automatic)', 'Credit card(automatic)'])
        MonthlyCharges = st.number_input(label='MonthlyCharges')
        TotalCharges = st.number_input(label='TotalCharges')
        submit_button = st.form_submit_button(label='Predict')
    return tenure, MonthlyCharges, TotalCharges, SeniorCitizen, gender, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, contract, PaperlessBilling, PaymentMethod, submit_button


#  function to transform TotalCharges using log1p
def log1p_transform(df):
    df['TotalCharges'] = np.log1p(df['TotalCharges'])
    return df

# select_model function
def select_model(gender, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, contract, PaperlessBilling, PaymentMethod):
    selected_model = st.session_state.get('selected_model', 'Catboost')
    pipeline, encoder = None, None
    try:  
        if selected_model == 'Catboost':
            pipeline = load_catboost()
        elif selected_model == 'Logistic':
            pipeline = load_logistic()
    except Exception as e:  # handling errors
        st.error(f"An error occurred loading the model: {e}")
    return pipeline, encoder

#data = [["gender", "Partner", "MonthlyCharges", "Dependents","TotalCharges", "SeniorCitizen","tenure", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "contract", "PaperlessBilling", "PaymentMethod"]]
 
database = st.secrets["database_name"]
server = st.secrets["server_name"]
username = st.secrets["Login"]
password = st.secrets["password"]

 

def LP2_Telco_churn():
    connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}"
    connection = pyodbc.connect(connection_string)
    #query
    query = 'SELECT * FROM dbo.LP2_Telco_churn_first_3000'
    data = pd.read_sql(query, connection)
    connection.close()

    return data

data = LP2_Telco_churn()


#  make_prediction function
def make_prediction(pipeline, data):
    if pipeline is not None:
        df = pd.DataFrame(data)
        df.to_csv('./Data/History.csv', mode='a', header=True, index=False if os.path.exists('./Data/History.csv') else True)
        if not os.path.exists:
            os.mkdir("./Data")
        df = log1p_transform(df)
        try:  
            prediction = pipeline.predict(df)[0]
            churn_probability = pipeline.predict_proba(df)[0][1]  
            prediction_label = "Churn😟" if prediction == 1 else "Not Churn😀"
            st.session_state.final_prediction = prediction_label
            st.session_state.final_probability = 100 * churn_probability
        except Exception as e:  # handling errors
            st.error(f"An error occurred making the prediction: {e}")



# Main function
def main():
    tenure, MonthlyCharges, TotalCharges, SeniorCitizen, gender, Partner, Dependents, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, contract, PaperlessBilling, PaymentMethod, submit_button = user_input_form()
    if submit_button:
        st.session_state.selected_model = st.selectbox(label='Select Model', options=['Catboost', 'Logistic'])
        pipeline, encoder = select_model(gender, Partner, Dependents, tenure, PhoneService, MultipleLines, InternetService, OnlineSecurity, OnlineBackup, DeviceProtection, TechSupport, StreamingTV, StreamingMovies, contract, PaperlessBilling, PaymentMethod)

        # Single-row DataFrame directly from user input values 
        df = pd.DataFrame({
            'gender': gender,
            'Partner': Partner,
            'Dependents': Dependents,
            'SeniorCitizen': SeniorCitizen,
            'MonthlyCharges': MonthlyCharges,
            'TotalCharges': TotalCharges,
            'tenure': tenure,
            'PhoneService': PhoneService,
            'MultipleLines': MultipleLines,
            'InternetService': InternetService,
            'OnlineSecurity': OnlineSecurity,
            'OnlineBackup': OnlineBackup,
            'DeviceProtection': DeviceProtection,
            'TechSupport': TechSupport,
            'StreamingTV': StreamingTV,
            'StreamingMovies': StreamingMovies,
            'Contract': contract,
            'PaperlessBilling': PaperlessBilling,
            'PaymentMethod': PaymentMethod
        }, index=[0]) 

        make_prediction(pipeline, df)
    # prediction and probability
    if st.session_state.final_prediction is not None:
        st.write(f'💫 Prediction of the customer to churn: {st.session_state.final_prediction}')
        st.write(f'✨ Probability that the customer will churn will be: {st.session_state.final_probability:.1f}%')


if __name__ == "__main__":
    main()
