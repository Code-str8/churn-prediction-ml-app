import streamlit as st
from  PIL import Image
import os
from auth import login_form, is_authenticated

st.set_page_config(
    page_icon= "✨",
    page_title= "Churn app",
    layout = "centered"
)


def main_page():
    login_form()
    if is_authenticated():
        st.write("Welcome!🎉")


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
    else:
     st.error("Please log in to access the App.")

if __name__ == "__main__":
    main_page()
