# IMPORTS
import streamlit as st
from functions.user_info_functions.pass_user_data import pass_user_data
from components.sidebar import sidebar_component_render
from components.stats_bar import stats_bar_component_render
from functions.validation_functions.sql_validation import validate_sql
from components.password_container import password_container_component_render
from functions.full_page_reload import full_page_reload
from functions.user_info_functions.load_user_passwords import load_user_passwords
from functions.user_info_functions.load_user_stats import load_user_stats


st.set_page_config(layout="wide") # to use full width of page

def dashboard_page():


    user_data = pass_user_data()

    load_user_passwords(user_data["username"]) 

    load_user_stats()


    #content for the navigation
    sidebar_component_render()

    # st.toast('Successful login', icon=':material/lock_person:')

    st.title("Welcome " + user_data["user_first_name"].title() + " 👋")

    stats_bar_component_render()

    password_search = st.text_input("Search for a password", label_visibility="hidden", placeholder="Search for a password...")


    # Initial render of all passwords
    if password_search == "":

        # Adds password id's and names to list and sorts them
        alphabetized_passwords = []
        for password_dict in user_data["user_passwords"]:
            alphabetized_passwords.append([password_dict["password_id"], password_dict["website_name"].lower()])
        alphabetized_passwords.sort(key=lambda x: x[1])

        # Renders password containers by finding password id in user_data["user_passwords"]
        for password_id_and_name in alphabetized_passwords:
            password_dict = next((p for p in user_data["user_passwords"] if p["password_id"] == password_id_and_name[0]), None)
            if password_dict != None:
                password_container_component_render(password_dict, "dashboard_page")
    else:
        if validate_sql(password_search):
            none_flag = False
            for password_dict in user_data["user_passwords"]:
                if password_search.lower() == (password_dict["website_name"].lower())[:len(password_search)]:
                    password_container_component_render(password_dict, "dashboard_page")
                    none_flag = True     
            if none_flag == False:
                st.error('No matching passwords found!', icon="🚨")
    

dashboard_page()