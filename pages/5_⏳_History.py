import streamlit as st
import pandas as pd 
import datatables
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

# Replace with your data persistence mechanism
history_df = pd.DataFrame({
    "Prediction Date": pd.to_datetime(["2023-01-10", "2023-02-05", "2023-02-15"]),
    "User Input_1": [123, 456, 789],
    "User Input_2": ["A", "B", "C"],
    "Prediction": ["High", "Low", "Medium"],
    "Prediction Confidence": [0.85, 0.72, 0.91],
    "Model Used": ["Model A", "Model B", "Model C"],
})

st.set_page_config(
    page_icon="⏳",
    page_title="History",
    layout="wide"
)

st.title("**HISTORY**")

# Custom search bar
search_term = st.text_input("Search history", key="search_term")
if search_term:
    filtered_df = history_df[
        (history_df["Prediction"].str.contains(search_term, case=False)) |
        (history_df["User Input_1"].str.contains(search_term, case=False)) |
        (history_df["User Input_2"].str.contains(search_term, case=False))
    ]
    # Update display with filtered data (e.g., cards, timeline)
    # (adapt these updates to your specific display functions)
    ...

# Interactive table
def display_table(df):
    # Use datatables or another library for interactive table
    st.write(datatables.DataTable(df, title="Previous Predictions and User Inputs"))

display_table(history_df)  # Initially display all data

# Card-based layout
def display_cards(df):
    cards = [
        st.card(
            f"Prediction {i+1}: {prediction}",
            user_input=f"User Input {i+1}: {user_input}",
            subheader=f"Model: {model}, Confidence: {confidence:.2f}",
        )
        for i, (prediction, user_input, model, confidence) in enumerate(zip(df["Prediction"], df["User Input_1"], df["Model Used"], df["Prediction Confidence"]))
    ]
    st.deck(cards)

display_cards(history_df)  # Initially display all data

# Filter
def filter_history(date_range=None, prediction=None, user_input=None):
    filtered_df = history_df.copy()
    if date_range:
        filtered_df = filtered_df[filtered_df["Prediction Date"].between(date_range[0], date_range[1])]
    if prediction:
        filtered_df = filtered_df[filtered_df["Prediction"].str.contains(prediction, case=False)]
    if user_input:
        filtered_df = filtered_df[(filtered_df["User Input_1"].str.contains(user_input, case=False)) |
                                  (filtered_df["User Input_2"].str.contains(user_input, case=False))]
    # Update displays (table, cards, timeline) with filtered data
    display_table(filtered_df)
    display_cards(filtered_df)

date_range_filter = st.date_input("Filter by Date Range", key="date_range_filter")
prediction_filter = st.selectbox("Filter by Prediction", history_df["Prediction"].unique(), key="prediction_filter")
user_input_filter = st.text_input("Filter by User Input", key="user_input_filter")

st.button("Filter", key="filter_button", on_click=filter_history, args=(date_range_filter, prediction_filter, user_input_filter))

#timeline view
st.timeline(history_df.sort_values("Prediction Date"), orientation="vertical", key="timeline", line_color="gray")

#chat
def plot_chart(df, x_col, y_col):
    fig = px.line(df, x=x_col, y=y_col)
    st.plotly_chart(fig, key=f"chart_{x_col}_{y_col}")

selected_x_col = st.selectbox("Select X-axis Variable", history_df.columns, key="chart_x_col")
selected_y_col = st.selectbox("Select Y-axis Variable", history_df.columns, key="chart_y_col")

if selected_x_col != selected_y_col:
    plot_chart(history_df, selected_x_col, selected_y_col)

#Pagination
# Assuming `per_page` is 3
st.pagination(history_df, per_page=3, key="pagination")

# Download CSV button