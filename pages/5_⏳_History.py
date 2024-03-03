import streamlit as st
import pandas as pd 
import plotly.express as px



st.set_page_config(
    page_icon="⏳",
    page_title="History",
    layout="wide"
)

st.title("**HISTORY**")
search_term = st.text_input("Search history", key="search_term")
def user_predict_history():
    file_path = "Data/History.csv"
    try:
        history_df = pd.read_csv(file_path,header=3) 
        history_df.columns = history_df.iloc[0]
        history_df = history_df.iloc[1:]
    except pd.errors.ParserError as e:
        st.error(f"Error parsing CSV: {e}")
        return None  

    return history_df

if __name__ == "__main__":

  history_df = user_predict_history()

if history_df is not None: 
        st.dataframe(history_df)
else:
    st.write("Unable to display history data due to errors.")