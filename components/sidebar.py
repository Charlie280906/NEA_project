# IMPORTS
import streamlit as st
from functions.entry_functions.fortune1000_list_creator import password_company_creator
from functions.validation_functions.blank_validation import validate_blank
from functions.validation_functions.sql_validation import validate_sql
from functions.validation_functions.password_validation import validate_password
from functions.entry_functions.add_password import add_password

def sidebar_component_render():
    with st.sidebar:
        st.image("img/logo.png")
        st.write("")
        with st.popover("Add password", icon=":material/add:", use_container_width=True):
            company = st.selectbox("Company:", options=password_company_creator(), index=None)
            instructions = st.empty()
            instructions.write("Chose 'Add another option...' to add a custom name")
            if company == "Add another option...":
                company = st.text_input("Enter company name:")
                instructions.empty()
            username = st.text_input("Username:")
            password = st.text_input("Password:", type="password")
            add_password_button = st.button("Save", icon=":material/bookmark:", use_container_width=True, type="primary")
            if add_password_button and validate_blank(username) and validate_blank(password) and validate_sql(username) and validate_sql(password) and validate_password(password):
                add_password(company, username, password)
            else:
                st.error('Please ensure your username and password are in the correct format!', icon="🚨")
        st.divider()
        st.page_link("pages/dashboard.py", label="Dashboard", icon=":material/home:")
        st.page_link("pages/score.py", label="Score", icon=":material/speed:")
        st.page_link("pages/generator.py", label="Generator", icon=":material/password:")
        st.divider()
        log_out_button = st.button("Log out", icon=":material/logout:", use_container_width=True)
        if log_out_button:
            st.switch_page("pages/login.py")
