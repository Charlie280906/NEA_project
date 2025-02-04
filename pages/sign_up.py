# IMPORTS
import streamlit as st
from functions.validation_functions.sql_validation import validate_sql
from functions.validation_functions.blank_validation import validate_blank
from functions.validation_functions.password_validation import validate_password
from functions.validation_functions.email_validation import validate_email
from functions.validation_functions.string_validation import validate_string
from functions.signup_function import signup_process

st.image("img/logo.png", width=300)

st.title("Sign Up")

with st.form("sign_up_form"): # form for users to enter sign up information
    col1, col2 = st.columns(2) # splits the container into 2 columns

    with col1:
        user_input_signup_fname = st.text_input(
        label="First name",
        placeholder="First name",
        label_visibility="hidden"
        )
        user_input_signup_email = st.text_input(
        label="Email",
        placeholder="Email",
        label_visibility="hidden"
        )
        user_input_signup_password= st.text_input(
        label="Password",
        placeholder="Password",
        label_visibility="hidden",
        type="password"
        )

    with col2:
        user_input_signup_lname = st.text_input(
        label="Last name",
        placeholder="Last name",
        label_visibility="hidden"
        )
        user_input_signup_username = st.text_input(
        label="Username",
        placeholder="Username",
        label_visibility="hidden"
        )
        user_input_signup_confirmed_password = st.text_input(
        label="Confirm password",
        placeholder="Confirm password",
        label_visibility="hidden",
        type="password"
        )

    st.write("")
    submit_form = st.form_submit_button("Sign up")
    st.write("")
    st.write("Already a PassSecure user? Log in [here](login)")

if submit_form: # runs code below once sign up button is clicked
    if validate_sql(user_input_signup_fname) and validate_sql(user_input_signup_lname) and validate_sql(user_input_signup_email) and validate_sql(user_input_signup_username) and validate_sql(user_input_signup_password) and validate_sql(user_input_signup_confirmed_password) and validate_blank(user_input_signup_fname) and validate_blank(user_input_signup_lname) and validate_blank(user_input_signup_email) and validate_blank(user_input_signup_username) and validate_blank(user_input_signup_password) and validate_blank(user_input_signup_confirmed_password) and validate_string(user_input_signup_fname) and validate_string(user_input_signup_lname) and validate_email(user_input_signup_email) and validate_password(user_input_signup_password) and validate_password(user_input_signup_confirmed_password): # checks valid inputs
        result = signup_process(user_input_signup_fname, user_input_signup_lname, user_input_signup_email, user_input_signup_username, user_input_signup_password, user_input_signup_confirmed_password) # runs sign up and stores result to determine next action
        if  result == "Success":
            st.switch_page("pages/dashboard.py") # redirects to dashboard pages, granting access
        if result == "ERROR! Connection":
            st.error('There is most likely an error with your username being duplicated. Please change it and try again. If not refresh the page as it may be a connection error!', icon="🚨")
        if result == "ERROR! Passwords":
            st.error('Make sure both passwords match and try again!', icon="🚨")
    else:
        st.error('Please ensure all your inputs are not empty and are in the correct format!', icon="🚨")