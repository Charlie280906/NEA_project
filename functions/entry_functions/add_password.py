# IMPORTS
from functions.user_info_functions.pass_user_data import pass_user_data
from functions.password_security_functions.password_scorer import score_password
from api.improve_password_function import improve_password
from functions.database_functions.database_push_function import database_push_request
from functions.user_info_functions.load_user_passwords import load_user_passwords
from functions.encryption.encrypt import encrypt
from streamlit_js_eval import streamlit_js_eval
from functions.password_security_functions.tag_checker import check_security_tags
from functions.full_page_reload import full_page_reload

# Function to add a new password entry for the user
def add_password(company, username, password):
    user_data = pass_user_data()

    password_scores = score_password(password)

    # Generate 5 improved versions of the user's password
    if password_scores[4] < 75:
        improved_versions = improve_password(password)
    else:
        improved_versions = None

    security_fields = check_security_tags(password, password_scores[4])

    table_name = f"{user_data['username']}_passwords"

    encryptedPass = encrypt(password)
    # Push the new password to the user's password table
    database_push_request(
        f"INSERT INTO `{table_name}` (website_name, password_username, password_password, length_score, number_score, case_score, symbol_score, overall_score, improved_password, security_fields) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (company, username, password, password_scores[0], password_scores[1], password_scores[2], password_scores[3], password_scores[4], str(improved_versions), str(security_fields))
    )


    full_page_reload()
