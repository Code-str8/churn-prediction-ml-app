import streamlit as st
from  PIL import Image
import os
st.set_page_config(
    page_icon= "✨",
    page_title= "Churn app",
    layout = "centered"
)


    
import streamlit as st

# Define CSS styles
css = """
<style>
    .auth-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 40px;
        background-color: #f2f2f2;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    .auth-title {
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .auth-input input {
        width: 100%;
        padding: 12px 20px;
        margin: 8px 0;
        display: inline-block;
        border: 1px solid #ccc;
        border-radius: 4px;
        box-sizing: border-box;
    }
    .auth-button button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        padding: 14px 20px;
        margin: 8px 0;
        border: none;
        border-radius: 4px;
        cursor: pointer;
    }
    .auth-button button:hover {
        background-color: #45a049;
    }
</style>
"""

# Add CSS to app
st.markdown(css, unsafe_allow_html=True)

def authenticate(username, password):
    # Simulate authentication (replace with your actual logic)
    if username == "admin" and password == "Admin01":
        return True
    else:
        return False

# Session state for authentication status
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

if not st.session_state["authenticated"]:
    with st.container():
        st.markdown("<div class='auth-title'>Login</div>", unsafe_allow_html=True)
        username = st.text_input("Username:", key="username")
        password = st.text_input("Password:", type="password", key="password")
        st.markdown("<div class='auth-input'></div>", unsafe_allow_html=True)
        st.markdown("<div class='auth-input'></div>", unsafe_allow_html=True)
        st.markdown("<div class='auth-button'></div>", unsafe_allow_html=True)
        login_button = st.button("Login")
        st.markdown("</div>", unsafe_allow_html=True)

        if login_button:
            if authenticate(username, password):
                st.session_state["authenticated"] = True
                st.success("Successfully logged in!")
            else:
                st.error("Invalid username or password.")
else:
    st.write("Welcome, you are now logged in!")

    st.title(f"**Customer Churn Predictor** :runner::department_store:")

    st.write(
        """
         Predict the likelihood of a customer leaving your business. This app uses machine learning to analyze data and identify customers at risk of churn.

        **Note:** This app is for demonstration purposes only. It does not provide real-time predictions.

        ### **Why is customer churn prediction important?**

        [Customer churn](https://www.questionpro.com/blog/customer-churn/) also known as customer attrition, can significantly impact your revenue and market share. By predicting churn, you can take proactive steps to retain customers and reduce its negative impact.


        
        **Key features:**

        * User-friendly interface
        * High accuracy machine learning models

        
        """
    )

    #image
    chun_img = Image.open(
        os.path.join (
            os.getcwd(),
            "assets/images/chun customer image.jpg"
            )
    )



    
    st.markdown(
        """
        #### **Benefits of Using This App**
        -  Gain early insights and make data-driven decisions to identify and retain at-risk customers.
        -  Personalized outreach: Tailor your retention strategies to specific needs and concerns.
        -  Improved ROI: Invest in retaining existing customers rather than acquiring new ones.

        """
    )

    

    # Call-to-action
    st.write("## Try it out❗") 
    st.write ("*Ready to start predicting churn?*:eyes:")

    # display GIF
    gif_path = 'assets/images/baby-scream meme.gif'
    st.image(
        gif_path, 
        caption='Retain Customers'
    )

    # Instructions
    st.write(
        """
        Head over to the [*DEMO* ](http://localhost:8501/Predict) to discover customer churn risk.

        For further details on the app's functionality and performance, explore the source code. 
        """
    )

# Link 
    st.write(
       """
    **Source Code:** [GitHub Repository](https://github.com/Code-str8/Churn-Prediction-ML-app)
      # Contact Me 📧
    **Gmail:** [ndunda.alex@gmail.com]
       """
    )
