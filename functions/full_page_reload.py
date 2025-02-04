# IMPORTS
from functions.user_info_functions.load_user_passwords import load_user_passwords
from functions.user_info_functions.pass_user_data import pass_user_data
from functions.user_info_functions.load_user_stats import load_user_stats
from streamlit_js_eval import streamlit_js_eval


def full_page_reload():
    user_data = pass_user_data()

    load_user_passwords(user_data["username"]) 

    load_user_stats()

    streamlit_js_eval(js_expressions="parent.window.location.reload()")