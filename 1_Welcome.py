import streamlit as st
from  PIL import Image

st.set_page_config(page_icon= "✨", page_title= "Churn app")
st.title(f"**Customer Chun Predictor** :runner::department_store:")
chun_img = Image.open(r"c:\Users\ndund\OneDrive\Pictures\chun customer image.jpg")
st.image(chun_img, use_column_width=True, caption= "negative experiences that can drive customers away.")

