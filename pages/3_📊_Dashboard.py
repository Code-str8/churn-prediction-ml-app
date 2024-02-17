import streamlit as st
import pandas as pd 
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(
    page_icon= "📊",
    page_title= "Dashboard",
    layout = "wide"
    )

st.title(f"**DASHBOARD📈**")
st.write(
        """
        Explore insightful visualizations and uncover key factors influencing customer churn on this interactive dashboards.
        """
    )

data = pd.read_excel("Dataset/Lp2_df_coc.xlsx")


# EDA Dashboard
def create_eda_dashboard(data):
    st.markdown(
    """
    ### **Univariate Analysis🔎**
    - [Univariate analysis](https://www.statisticshowto.com/univariate/) is a statistical technique that involves the analysis of a single variable.  In this section, we will perform univariate analysis on different variables to understand their relationships with each
    """)
    # Feature distribution
    st.subheader("Distribution of Features")
    fig, axes = plt.subplots(figsize=(12, 8))
    data.hist(ax=axes, grid=False, color="skyblue")
    plt.tight_layout()  
    st.pyplot(fig)
    st.markdown("""
    Insight📢: The visualization reveals the distributions of continuous numerical columns are notably uneven, predominantly exhibiting positive skewness.
    This observation suggests that these columns may benefit from transformations to achieve a more balanced distribution, which can positively impact the performance of machine learning models.
    """)

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
    st.markdown("Insight📢: The histogram above illustrates the distribution of senior citizens.")

    # Distribution of PhoneService
    st.subheader("Distribution of PhoneService")
    fig_phone = px.histogram(data, x="PhoneService", color="PhoneService", title="Distribution of PhoneService")
    st.plotly_chart(fig_phone)
    st.markdown("Insight📢: The histogram above illustrates the distribution of phone services.")

    # Distribution of InternetService
    st.subheader("Distribution of InternetService")
    fig_internet = px.histogram(data, x="InternetService", color="InternetService", title="Distribution of InternetService")
    st.plotly_chart(fig_internet)
    st.markdown("Insight📢: The histogram above illustrates the distribution of internet services.")

    st.markdown(
    """
    ### **Bi-variate Analysis🔎**
    - [Bivariate analysis](https://en.wikipedia.org/wiki/Bivariate_analysis) is the analysis of two variables to determine their relationship or correlation. 
      *Correlation* measures how closely two variables are related to each other. A positive correlation means that as one variable goes up, the other variable tends to go up too. 
    """)

    # Relationship among features - Correlation Matrix
    correlation_matrix = data.corr(numeric_only=True)

    # Plot heatmap
    st.subheader("Correlation Matrix of Continuous Features")
    fig_corr = px.imshow(correlation_matrix, color_continuous_scale='icefire')
    st.plotly_chart(fig_corr)
    st.markdown("""
    Insight📢: In this heatmap, we observe the correlation matrix of continuous features.
    Notably, the 'TotalCharges' column exhibits a moderate correlation with both 'tenure' and 'MonthlyCharges.'
    Similarly, the 'Partner' column demonstrates a moderate correlation with the 'Dependents' column.
    This insight can be leveraged for in-depth analysis and feature engineering, particularly when exploring and enhancing relationships among the mentioned columns.
    """)

    # Create a contingency table for Contract and Churn
    st.subheader("Contingency Table: Contract vs Churn")
    contingency_table = pd.crosstab(data['Contract'], data['Churn'])
    fig_contingency_contract = px.imshow(contingency_table, color_continuous_scale='icefire')
    st.plotly_chart(fig_contingency_contract)
    st.markdown("""
    Insight📢: The contingency table illustrates the distribution of the 'Contract' variable in rows and the 'Churn' variable in columns.
    When visualized using a heatmap, a notable observation emerges: there is a positive correlation between the contract length of 'Month-to-Month' and 'False' churn but mid relationship with 'True' churn.
    This observation aligns closely with our initial hypothesis.
    """)

    # Create a contingency table for PaymentMethod and Churn
    st.subheader("Contingency Table: PaymentMethod vs Churn")
    contingency_table2 = pd.crosstab(data['PaymentMethod'], data['Churn'])
    fig_contingency_payment = px.imshow(contingency_table2, color_continuous_scale='icefire')
    st.plotly_chart(fig_contingency_payment)
    st.markdown("""
    Insight📢: Utilizing a heatmap, we visualized the distribution of the 'Contract' variable in rows and the 'Churn' variable.
    Notably, we observed that the Payment Method categorized as 'Automatic' demonstrates a positive correlation with 'False' churn.
    Additionally, the Payment Method labeled as 'Electronic check' exhibits a moderate correlation with 'True' churn and a positive correlation with 'False' churn.
    This evidence provides valuable insights that can be employed to address and validate our initial hypothesis.
    """)

# KPIs Dashboard
def create_kpis_dashboard(data):
    st.markdown(
    """
    ## Key Performance Indicators (KPIs) 📈� 
    🌟 How do contract terms and payment methods correlate with customer churn?        
    """)

    # Contingency table
    contingency_table3 = pd.crosstab(index=data['Contract'], columns=[data['PaymentMethod'], data['Churn']])
    # Plot heatmap
    fig_contingency3 = px.imshow(contingency_table3, color_continuous_scale='icefire')
    st.subheader('Correlation between Contract, Payment Method, and Churn')
    st.plotly_chart(fig_contingency3)
    st.markdown("""
    Insight📢: Based on the observed data, the Contract term of 'Two Year' exhibits a moderate correlation with both variables: 'Churn' (False) and 'PaymentMethod' (Automatic).
    Conversely, the Contract term of 'Month-to-month' shows a positive correlation with both variables: 'Churn' (True) and 'PaymentMethod' (Electronic check).
    This evidence supports the hypothesis that customers with longer contract terms (Two Year) are less likely to churn (Churn=False) and are more inclined to use automatic payment methods.
    On the other hand, customers with shorter, month-to-month contracts are more likely to churn (Churn=True) and tend to prefer the Electronic check payment method.
    """)

    st.markdown(
    """ 
    🌟 Are there specific services that significantly impact churn rates?       
    """)
    
    # Bar plot for InternetService
    fig_internet = px.bar(data, x='InternetService', color='Churn', barmode='group', color_discrete_map={True:'orange', False:'blue'})
    fig_internet.update_layout(title='Impact of InternetService on Churn Rates')
    st.plotly_chart(fig_internet)

    # Bar plot for PhoneService
    fig_phone = px.bar(data, x='PhoneService', color='Churn', barmode='group', color_discrete_map={True:'orange', False:'blue'})
    fig_phone.update_layout(title='Impact of PhoneService on Churn Rates')
    st.plotly_chart(fig_phone)
    st.markdown("Insight📢: In the analysis, two services, namely (InternetService) and (PhoneService), were selected. The visualization clearly indicates a positive impact on the Churn rate, with the majority showing a False Churn. This observation strongly supports the notion that specific services play a significant role in influencing the Churn rate.")
 
    st.markdown(
    """ 
    🌟 Are there specific services that customers with longer contract terms tend to use more frequently?     
    """)

    # Subplots
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))
    sns.countplot(x='Contract', hue='InternetService', data=data, palette={'Fiber optic':'orange','DSL':'blue','No':'red'}, ax=axes[0])
    axes[0].set_title('Internet Service by Contract Term')
    sns.countplot(x='Contract', hue='PhoneService', data=data, palette={'Yes':'orange', 'No':'blue'}, ax=axes[1])
    axes[1].set_title('Phone Service by Contract Term')
    st.pyplot(fig)
    st.markdown("""
    Insight📢: Analyzing the bar plot for two services, namely (InternetService) and (PhoneService), it is evident that customers with longer contract terms predominantly opt for Fiber Optic in the case of internet service and utilize phone services more frequently. This observation suggests that longer contract terms have a positive influence on the selected services.
    """)

    st.markdown(
    """ 
    🌟 Do customers using automatic payment methods show different churn patterns compared to other payment methods?     
    """)

    # Histogram with Plotly
    fig_payment = px.histogram(data, x='PaymentMethod', color='Churn', barmode='stack', color_discrete_map={True:'orange', False:'blue'}, labels={'PaymentMethod': 'Payment Method', 'Churn': 'Churn'}, title='Churn Patterns by Payment Method')
    fig_payment.update_layout(xaxis_title='Payment Method', yaxis_title='Count', showlegend=True)
    st.plotly_chart(fig_payment)
    st.markdown("""
    Insight📢: Upon examining the diverse churn patterns based on customer payment methods, it is evident that customers using the (automatic) payment method exhibit a False churn pattern. In contrast, the (Electronic check) payment method shows a True churn pattern. This provides valuable insights in line with the hypothesis.
    """)
    
    st.markdown(
    """ 
    🌟 Are senior citizens more or less likely to churn compared to non senior citizens?     
    """)

    # Mean churn rates for senior citizens and non-senior citizens
    senior_churn_rate = (data[data['SeniorCitizen'] == 1]['Churn'] == 'Yes').mean()  # Convert 'Yes' to 1, 'No' to 0
    non_senior_churn_rate = (data[data['SeniorCitizen'] == 0]['Churn'] == 'Yes').mean()  # Convert 'Yes' to 1, 'No' to 0

    # Plot pie chart
    labels = ['Senior Citizen', 'Non-Senior Citizen']
    sizes = [senior_churn_rate, non_senior_churn_rate]
    colors = ['blue', 'orange']
    fig_pie, ax_pie = plt.subplots(figsize=(8, 8))
    ax_pie.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax_pie.set_title('Churn Rates by Senior Citizen Status')
    st.pyplot(fig_pie)
    st.markdown("""
    Insight📢: The chart above clearly indicates that Senior Citizens are less likely to churn, with a churn rate of 63.4%, in comparison to non-Senior Citizens.
    This insight can be leveraged for strategic considerations.
    """)


# Dashboard selection
st.sidebar.header("Select Dashboard Type:")
dashboard_type = st.sidebar.selectbox("", ["EDA", "KPIs"])

if dashboard_type == "EDA":
    create_eda_dashboard(data)
elif dashboard_type == "KPIs":
    create_kpis_dashboard(data)
else:
    st.error("Invalid dashboard type.")