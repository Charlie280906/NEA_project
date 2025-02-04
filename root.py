# IMPORTS
import json
import streamlit as st

empty_structure = {
    "username": "",
    "user_email": "",
    "user_password": "",
    "user_first_name": "",
    "user_last_name": "",
    "encryption_keys": "",
    "user_stats": [],
    "user_passwords": []
}

with open("json/full_user_info.json", "w") as json_file:
    json.dump(empty_structure, json_file, indent=4)

st.switch_page("pages/login.py")

# TODO: comment main chunks in all files (use gpt)
# TODO: remove unnecessary lines of code
# TODO: write up evaluation for iteration 9


