# IMPORTS
import streamlit as st
from functions.validation_functions.sql_validation import validate_sql
from functions.validation_functions.password_validation import validate_password
from functions.validation_functions.blank_validation import validate_blank
from functions.login_function import login_authentication

st.image("img/logo.png", width=300)

st.title("Log In")

with st.form("log_in_form"): # form for users to enter log in information
    user_input_login_username = st.text_input(
        label="Username",
        placeholder="Username",
        label_visibility="hidden"
    )
    user_input_login_password = st.text_input(
        label="Password",
        placeholder="Password",
        label_visibility="hidden",
        type="password"
    )
    st.write("")
    submit_form = st.form_submit_button("Log in")
    st.write("")
    st.write("Haven't used PassSecure before? Sign up [here](sign_up)")

if submit_form: # runs code below once log in button is clicked
    if validate_sql(user_input_login_username) and validate_sql(user_input_login_password) and validate_blank(user_input_login_username) and validate_blank(user_input_login_password) and validate_password(user_input_login_password): # checks valid inputs
        if login_authentication(user_input_login_username, user_input_login_password): # authenticates user with db
            st.switch_page("pages/dashboard.py") # redirects to dashboard pages, granting access
        else:
            st.error('Cannot find you as a user! Do you need to sign up?', icon="🚨")
    else:
        st.error('Please ensure your email and password are in the correct format!', icon="🚨")