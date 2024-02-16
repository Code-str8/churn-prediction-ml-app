import streamlit as st
import pandas as pd 



st.set_page_config(
    page_icon="📚",
    page_title="Datos",
    layout="wide"
)

st.sidebar.header("Select Language:")
language = st.sidebar.selectbox("", ["English", "Español"])

if language == "Español":
    st.title(f"**Explora tus Datos de Cliente⭐**")
    st.write(
        """
        Obtén valiosos conocimientos sobre tu base de clientes y comprende los factores que afectan la rotación con esta página de datos interactiva.
        """
    )

    # Upload a excel
    data = pd.read_excel("Dataset/Lp2_df_coc.xlsx")
    st.dataframe(data)

    numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'SeniorCitizen']
    categorical_features = ['gender', 'Partner', 'Dependents', 'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod']

    selected_feature_type = st.radio("Seleccionar Tipo de Característica:", ["Numérico", "Categórico"])

    if selected_feature_type == "Numérico":
        selected_feature = st.selectbox("Seleccionar una Característica Numérica", numeric_features)
        st.write(
            f"**Explorando Característica Numérica: {selected_feature}**"
        )
    elif selected_feature_type == "Categórico":
        selected_feature = st.selectbox("Seleccionar una Característica Categórica", categorical_features)
        st.write(
            f"**Explorando Característica Categórica: {selected_feature}**"
        )
    else:
        st.error("Tipo de característica inválido.")

    # Feature explanations
    st.header("Explicación de Características")
    st.write(
        """
        Haz clic en el nombre de una característica para ver su descripción e impacto potencial en la rotación:
        """
    )
    column_descriptions = {
        "customerID": "🆔 Identificador único para cada cliente.",
        "tenure": "🔁 Número de meses que el cliente ha estado con la empresa.",
        "MonthlyCharges": "💲 La cantidad cobrada a la cuenta del cliente cada mes.",
        "TotalCharges": "💰 La cantidad total cobrada a la cuenta del cliente.",
        "Churn": "🔚 Si el cliente ha abandonado (dejado la empresa) o no. Un valor de 1 indica abandono, mientras que un valor de 0 indica que no hay abandono.",
        "gender": "🚻 Si el cliente es hombre o mujer.",
        "SeniorCitizen": "👤 Si el cliente es una persona mayor o no",
        "Partner": "👫 Si el cliente tiene pareja o no.",
        "Dependents": "👪 Si el cliente tiene dependientes o no (Sí, No)",
        "PhoneService": "☎️ Si el cliente tiene servicio telefónico o no (Sí, No)",
        "MultipleLines": "📲 ¿El cliente tiene líneas múltiples? (Sí, No)",
        "InternetService": "📡 Tipo de servicio de internet utilizado por el cliente (Fibra óptica, DSL, No) ",
        "OnlineSecurity": "🔐 ¿Se proporciona seguridad en línea para el cliente? (Sí, No, Sin internet)",
        "OnlineBackup": "📶 ¿El cliente tiene copia de seguridad en línea? (Sí, No, Sin internet)",
        "DeviceProtection": "🔐 ¿La empresa ofrece protección de dispositivos? (Sí, No, Sin servicio de internet)",
        "TechSupport": "👋 ¿Hay soporte técnico disponible para los clientes? (Sí, No, Sin internet).",
        "StreamingTV": "📺 ¿El cliente usa TV en streaming? (Sí, No, Sin servicio de internet)",
        "StreamingMovies": "🎥 ¿El cliente usa películas en streaming? (Sí, No, Sin servicio de internet)",
        "Contract": "📃 Término del contrato del cliente (Mensual, Anual, Bienal)",
        "PaperlessBilling": "📃 Si el cliente tiene facturación sin papel o no (Sí, No)",
        "PaymentMethod": "💳 Método de pago del cliente (Cheque electrónico, cheque enviado por correo, Transferencia bancaria (automática), Tarjeta de crédito (automática))"
    }

    feature_explanation = st.selectbox("", data.columns)
    st.write(f"**{feature_explanation}:** {column_descriptions.get(feature_explanation, 'No disponible')}")
    st.write(f"**{feature_explanation}:** {data[feature_explanation].describe()}")

    st.markdown(
        """
        <div style="text-align: center;">
        <a href="/Dashboard" class="btn btn-primary">¡Nos vemos en la siguiente página!</a>
        </div>
        """,
        unsafe_allow_html=True
    )
    # display GIF
    gif_path = 'assets/images/pepe meme.gif'
    st.image(
        gif_path
    )
else:
    # Translate content to English
    st.title(f"**Explore Customer Data⭐**")
    st.write(
        """
        Gain valuable insights into customer base and understand factors affecting churn with this interactive data page.
        """
    )

    # Upload a excel
    data = pd.read_excel("Dataset/Lp2_df_coc.xlsx")
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