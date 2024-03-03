import streamlit as st
import pandas as pd 
import plotly.express as px

st.set_page_config(
    page_icon= "⏳",
    page_title= "History",
    layout = "wide"
    )

st.title(f"**HISTORY**")
st.write (
    """
    """
)


def user_predict_history():
    file_path = "./Data/History.csv"
    history_df = pd.read_csv(file_path)
    return history_df

if __name__=="__main__":
    
    history_df = user_predict_history()
    st.dataframe(history_df)