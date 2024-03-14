
import streamlit as st

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

def authenticate(username, password):
   
    if username == "admin" and password == "Admin01":
        return True
    else:
        return False

def login_form():
    st.markdown(css, unsafe_allow_html=True)

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
        st.write(" ")

def is_authenticated():
    return st.session_state.get("authenticated", False)

