import streamlit as st
import pandas as pd 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import pyodbc
from auth import login_form, is_authenticated

st.set_page_config(
    page_icon= "📊",
    page_title= "Dashboard",
    layout = "wide"
    )

def dashboard_page():
    login_form()
    if is_authenticated():
        st.title(f"**DASHBOARD📈🔎**")
        st.write(
         """
         Explore insightful visualizations and uncover key factors influencing customer churn on this interactive dashboards.
         """
        )

        data = pd.DataFrame(pd.read_excel("Lp2_df_coc.xlsx"))

        # EDA Dashboard
        def create_eda_dashboard(data):
          # Feature distribution
           st.subheader("Distribution of Features")
           fig, axes = plt.subplots(figsize=(12, 8))
           data.hist(ax=axes, grid=False, color="skyblue")
           plt.tight_layout()
           st.pyplot(fig)
    

          # Contract distribution
           fig_contract = px.bar(data, x="Contract", color="Churn")
           fig_contract.update_layout(title="Distribution of Churn by Contract")
           st.plotly_chart(fig_contract)

          # Payment method distribution
           fig_payment = px.bar(data, x="PaymentMethod", color="Churn")
           fig_payment.update_layout(title="Distribution of Churn by Payment Method")
           st.plotly_chart(fig_payment)

          # Distribution of SeniorCitizen
           st.subheader("Distribution of SeniorCitizen")
           fig_senior = px.histogram(data, x="SeniorCitizen", color="SeniorCitizen", title="Distribution of SeniorCitizen")
           st.plotly_chart(fig_senior)
    

          # Distribution of PhoneService
           st.subheader("Distribution of PhoneService")
           fig_phone = px.histogram(data, x="PhoneService", color="PhoneService", title="Distribution of PhoneService")
           st.plotly_chart(fig_phone)
   
          # Distribution of InternetService
           st.subheader("Distribution of InternetService")
           fig_internet = px.histogram(data, x="InternetService", color="InternetService", title="Distribution of InternetService")
           st.plotly_chart(fig_internet)
    

    

          # Relationship among features - Correlation Matrix
           correlation_matrix = data.corr(numeric_only=True)

          # Plot heatmap
           st.subheader("Correlation Matrix of Continuous Features")
           fig_corr = px.imshow(correlation_matrix, color_continuous_scale='icefire')
           st.plotly_chart(fig_corr)
    

          # Create a contingency table for Contract and Churn
           st.subheader("Contingency Table: Contract vs Churn")
           contingency_table = pd.crosstab(data['Contract'], data['Churn'])
           fig_contingency_contract = px.imshow(contingency_table, color_continuous_scale='icefire')
           st.plotly_chart(fig_contingency_contract)
    

          # Create a contingency table for PaymentMethod and Churn
           st.subheader("Contingency Table: PaymentMethod vs Churn")
           contingency_table2 = pd.crosstab(data['PaymentMethod'], data['Churn'])
           fig_contingency_payment = px.imshow(contingency_table2, color_continuous_scale='icefire')
           st.plotly_chart(fig_contingency_payment)
    

        # KPIs Dashboard
        def create_kpis_dashboard(data):

          # Contingency table
            contingency_table3 = pd.crosstab(index=data['Contract'], columns=[data['PaymentMethod'], data['Churn']])
          # Plot heatmap
            fig_contingency3 = px.imshow(contingency_table3, color_continuous_scale='icefire')
            st.subheader('Correlation between Contract, Payment Method, and Churn')
            st.plotly_chart(fig_contingency3)
    

    
    
          # Bar plot for InternetService
            fig_internet = px.bar(data, x='InternetService', color='Churn', barmode='group', color_discrete_map={True:'orange', False:'blue'})
            fig_internet.update_layout(title='Impact of InternetService on Churn Rates')
            st.plotly_chart(fig_internet)

          # Bar plot for PhoneService
            fig_phone = px.bar(data, x='PhoneService', color='Churn', barmode='group', color_discrete_map={True:'orange', False:'blue'})
            fig_phone.update_layout(title='Impact of PhoneService on Churn Rates')
            st.plotly_chart(fig_phone)
    

          # Subplots
            fig, axes = plt.subplots(1, 2, figsize=(12, 6))
            sns.countplot(x='Contract', hue='InternetService', data=data, palette={'Fiber optic':'orange','DSL':'blue','No':'red'}, ax=axes[0])
            axes[0].set_title('Internet Service by Contract Term')
            sns.countplot(x='Contract', hue='PhoneService', data=data, palette={True:'orange', False:'blue'}, ax=axes[1])
            axes[1].set_title('Phone Service by Contract Term')
            st.pyplot(fig)
   
        def create_kpis(data):
            total_customers = len(data)
            churn_customers = data[data['Churn'] == True].shape[0]
            non_churn_customers = data[data['Churn'] == False].shape[0]
            churn_rate = round((churn_customers / total_customers) * 100, 2)

            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Customers", total_customers)
            col2.metric("Churn Customers", churn_customers)
            col3.metric("Non-Churn Customers", non_churn_customers)
            col4.metric("Churn Rate (%)", str(churn_rate) + "%")
    
    
   

        # Dashboard selection
        st.sidebar.header("Select Dashboard Type:")
        dashboard_type = st.sidebar.selectbox("", ["EDA", "KPIs"])

        if dashboard_type == "EDA":
          create_eda_dashboard(data)
        elif dashboard_type == "KPIs":
          create_kpis(data)
          create_kpis_dashboard(data)
        else:
          st.error("Invalid dashboard type.")
    else:
     st.error("Please log in to access the App. Username: admin Password: Admin01")

if __name__ == "__main__":
    dashboard_page()