import streamlit as st
import pandas as pd 
import pyodbc
import warnings
warnings.filterwarnings("ignore")


st.set_page_config(
    page_icon="📚",
    page_title="Datos",
    layout="wide"
)


# Translate content to English
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


st.title(f"**Explore Customer Data⭐**")
st.write(
        """
        Gain valuable insights into customer base and understand factors affecting churn with this interactive data page.
        """
    )

    
st.dataframe(data)

numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen']
categorical_features = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']

selected_feature_type = st.radio("Select Feature Type:", ["Numerical", "Categorical"])

if selected_feature_type == "Numerical":
        selected_feature = st.selectbox("Select a Numeric Feature", numeric_features)
        st.write(
            f"**Exploring Numerical Feature: {selected_feature}**"
        )
elif selected_feature_type == "Categorical":
        selected_feature = st.selectbox("Select a Categorical Feature", categorical_features)
        st.write(
            f"**Exploring Categorical Feature: {selected_feature}**"
        )
else:
        st.error("Invalid feature type.")

# Feature explanations
st.header("Feature Explanations")
st.write(
        """
        Click on a feature name to view its description and potential impact on churn:
        """
    )
column_descriptions = {
        "customerID": "🆔 Unique identifier for each customer.",
        "tenure": "🔁 Number of months the customer has been with the company.",
        "MonthlyCharges": "💲 The amount charged to the customer's account each month.",
        "TotalCharges": "💰 The total amount charged to the customer's account.",
        "Churn": "🔚 Whether the customer has churned (left the company) or not. A value of 1 indicates churn, while a value of 0 indicates no churn.",
        "gender": "🚻 Whether the customer is a male or a female.",
        "SeniorCitizen": "👤 Whether a customer is a senior citizen or not",
        "Partner": "👫 Whether the customer has a partner or not.",
        "Dependents": "👪 Whether the customer has dependents or not (Yes, No)",
        "PhoneService": "☎️ Whether the customer has a phone service or not (Yes, No)",
        "MultipleLines": "📲 Does the customer have multiple lines? (Yes, No)",
        "InternetService": "📡 Type of internet service used by the customer (Fiber optic, DSL, No) ",
        "OnlineSecurity": "🔐 Is online security provided for the customer? (Yes, No, No Internet)",
        "OnlineBackup": "📶 Does the customer have online backup? (Yes, No, No Internet)",
        "DeviceProtection": "🔐 Is device protection offered by the company? (Yes, No, No Internet service)",
        "TechSupport": "👋 Is technical support available to customers? (Yes, No, No Internet).",
        "StreamingTV": "📺 Does the customer use streaming TV? (Yes, No, No Internet service)",
        "StreamingMovies": "🎥 Does the customer use streaming movies? (Yes, No, No Internet service)",
        "Contract": "📃 The contract term of the customer (Month-to-Month, One year, Two year)",
        "PaperlessBilling": "📃 Whether the customer has paperless billing or not (Yes, No)",
        "PaymentMethod": "💳 The customer payment method (Electronic check, mailed check, Bank transfer(automatic), Credit card(automatic))"
    }

feature_explanation = st.selectbox("", data.columns)
st.write(f"**{feature_explanation}:** {column_descriptions.get(feature_explanation, 'No description available')}")
st.write(f"**{feature_explanation}:** {data[feature_explanation].describe()}")

st.markdown(
        """
        <div style="text-align: center;">
        <a href="/Dashboard" class="btn btn-primary">See You In The Next Page!</a>
        </div>
        """,
        unsafe_allow_html=True
    )
# display GIF
gif_path = 'assets/images/pepe meme.gif'
st.image(
    gif_path
)