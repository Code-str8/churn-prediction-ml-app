import streamlit as st
from  PIL import Image
import os
st.set_page_config(
    page_icon= "✨",
    page_title= "Churn app",
    layout = "centered"
)

st.title(f"**Customer Chun Predictor** :runner::department_store:")

# Description 
st.write(
    """
This app predicts the likelihood of a customer churning. It uses a machine learning model trained on a dataset of customer features. The model predicts whether a customer will churn or not based on the input features.

**Note:** This app is for demonstration purposes only. It does not provide real-time predictions.

### **Why is customer churn prediction important?**

[Customer churn](https://www.questionpro.com/blog/customer-churn/) also known as customer attrition, is the loss of customers over a given period of time. It is a common problem faced by businesses and can have significant consequences, including a decline in revenue and a loss of market share.

By using machine learning to predict customer churn, businesses can take proactive steps to retain customers and reduce the negative impact of churn.

#### **How does the app work?**

The app allows you to input a variety of customer features, such as Tenure,Contract type, and Total charges. Based on these features, the machine learning model will predict whether a customer is at risk of churning.

**Key features:**

* User-friendly interface
* High accuracy machine learning models

**Model performance:**

Our machine learning models have been trained on a large dataset of customer features and has achieved an accuracy of 80%.
"""
)
#image
chun_img = Image.open(
    os.path.join (
        os.getcwd(),
        "assets/images/chun customer image.jpg"
        )
)

#display img
st.image(
    chun_img,
    use_column_width=True,
    caption= "Bees represent negative experiences that can drive customers away."
)

#st.header("Benefits of Using This App:")
st.markdown(
    """
    #### **Benefits of Using This App:**
    - **Early warnings:** Gain insights into which customers are at risk of leaving, allowing you to intervene before it's too late.
    - **Data-driven decisions:** Base your retention efforts on objective predictions, not just intuition.
    - **Personalized outreach:** Tailor your retention strategies to the specific needs and concerns of at-risk customers.
    - **Improved ROI:** Invest in retaining existing customers rather than acquiring new ones, often at a lower cost.
    """
)

# Call-to-action
st.write("## Try it out❗") 
st.write ("*Ready to start predicting churn?*:eyes:")

# display GIF
gif_path = 'assets/images/hell-yeah-hell-to-the-yeah meme.gif'
st.image(
    gif_path, 
    caption='Below Identify & Retain Happy Customers'
)

# Instructions
st.write(
    """
    Head over to the [*Predict page* ](http://localhost:8501/Predict) to easily input customer information and discover their churn risk.

    For further details on the app's functionality and performance, explore the **Welcome** page. 
    """
)

# Link 
st.write(
    """
**Source Code:** [GitHub Repository](https://github.com/Code-str8/Churn-Prediction-ML-app)
"""
)
