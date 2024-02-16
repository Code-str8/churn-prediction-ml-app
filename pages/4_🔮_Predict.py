import streamlit as st
import pandas as pd
import joblib  
import os
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

