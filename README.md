<a name="readme-top"></a>

<div align="center">
  <h1><b>✨Churn-Prediction-ML-app</b></h1>
</div>



### 📘Table of Contents
1. [Setup](#setup)
2. [Running the App](#running-the-app)
3. [Usage](#usage)
    - [Welcome Page](#welcome-page)
    - [Login Page](#login-page)
    - [Data Page](#data-page)
    - [Predictor Page](#predictor-page)
    - [Dashboard Page](#dashboard-page)
    - [History Page](#history-page)
4. [Models Used](#models-used)
5. [Deployment](#deployment)
6. [Further Development](#further-development)
7. [Contributing](#contributing)
8. [License](#license)


# 📱➡️ Churn Predictor <a name="about-project"></a>

**Churn Predictor** a machine learning application using Streamlit to predict customer churn in a telecommunications company. This tool leverages predictive analytics to identify potential churners among subscribers. With Streamlit's interactive interface, stakeholders can easily explore churn prediction results, enabling proactive measures to retain customers

Features
1. **Gender**: Whether the customer is a male or a female
2. **SeniorCitizen**: Employee attrition status
3. **Partner**: Whether the customer has a partner or not (Yes, No);
4. **Dependents**: Whether the customer has dependents or not (Yes, No);
5. **Tenure**: Number of months the customer has stayed with the company;
6. **PhoneService**: Whether the customer has phone service or not (Yes, No);
7. **MultipleLines**: Whether the customer has multiple lines;
8. **InternetService**: Customer’s internet service provider (DSL, Fiber Optic, No);
9. **OnlineSecurity**: Whether the customer has online security or not (Yes, No, No Internet);
10. **OnlineBackup**: Whether the customer has online backup or not (Yes, No, No Internet);
11. **DeviceProtection**: Whether the customer has device protection or not (Yes, No, No internet service);
12. **TechSupport**: Whether the customer has tech support or not (Yes, No, No internet);
13. **StreamingTV**: Whether the customer has streaming TV or not (Yes, No, No internet service);
14. **StreamingMovies**: Whether the customer has streaming movies or not (Yes, No, No Internet service);
15. **Contract**: The contract term of the customer (Month-to-Month, One year, Two year);
16. **PaperlessBilling**: Whether the customer has paperless billing or not (Yes, No);
17. **PaymentMethod**: The customer’s payment method (Electronic check, Mailed check, Bank transfer(automatic), Credit card(automatic));
18. **MonthlyCharges**: The amount charged to the customer monthly;
19. **TotalCharges**: The total amount charged to the customer;
20. **Churn**: Whether the customer churned or not (Yes or No).

### Setup🔧 <a name="setup"></a>
 
1. **Clone Repository**: Clone the repository containing the Streamlit app code.
2. **Install Dependencies**: Install the required dependencies using pip.
3. **Data Setup**: Ensure you have a CSV dataset named `Lp2_df_coc.xlsx` placed inside a folder named `dataset` in the project directory.
 
### 💻 Running the App <a name="running-the-app"></a>
 
To run the app locally, execute the following command in the project directory:
 
```bash
streamlit run 1_Welcome.py
```
 
The app will start running locally and can be accessed through a web browser.
 
### Usage <a name="usage"></a>
 
#### Welcome Page <a name="welcome-page"></a>
- Provides an overview of the app and its purpose.
 
#### Login Page <a name="login-page"></a>
- New Users: Enter username and password to log in.
- Credential: Username=admin and password=Admin01.
 
#### 📚 Data Page <a name="data-page"></a>
- Displays basic information about the dataset.
- Shows summary statistics of numerical variables.
- Provides the first few rows of the dataset.
- Conducts univariate and bivariate analysis.
- Presents additional analysis using pandas styling.
 
#### 🔮 Predict Page <a name="predictor-page"></a>
- Online Prediction: Input customer details interactively to predict churn.
 
#### 📊 Dashboard Page <a name="dashboard-page"></a>
- Provides visualizations and analytics related to customer churn.
- Includes research questions and key performance indicators.
- Offers insights through various charts and plots.
 
#### ⏳ History Page <a name="history-page"></a>
- Tracks user interactions with the app.
- Displays a history log of actions performed by the user.
- Allows navigating back to previous points in history.
 
### Models Used <a name="models-used"></a>
 
#### Supported Models
1. Logistic Regression
2. CatBoost
 
#### Description
- Logistic Regression: Supervised machine learning algorithm used for classification tasks.
- CatBoost: Implementation of gradient boosted decision trees designed for speed and performance.
 
#### Model Training
- Data Preprocessing
- Pipeline Creation
- Model Training
- Evaluation
 
#### Model Selection
- User Choice
- Performance Comparison
 
### 🎉Deployment <a name="deployment"></a>
 
- Model Serialization
- Model Loading
 
### Further Development <a name="further-development"></a>
 
- Model Tuning
- Model Expansion
- Model Monitoring
 
### 💡Contributing <a name="contributing"></a>
 
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or create a pull request.
 
### 🔐 License <a name="license"></a>
 
This project is licensed under the [MIT](LICENSE). Feel free to use, modify, and distribute the code for personal and commercial purposes.
