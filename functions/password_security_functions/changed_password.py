# IMPORTS
from functions.password_security_functions.password_scorer import score_password
from api.improve_password_function import improve_password
from functions.user_info_functions.pass_user_data import pass_user_data
from functions.database_functions.database_push_function import database_push_request
from functions.password_security_functions.tag_checker import check_security_tags
from functions.user_info_functions.load_user_passwords import load_user_passwords
from streamlit_js_eval import streamlit_js_eval
from functions.full_page_reload import full_page_reload

def changed_password(improved_password, password_dict_id):

    user_data = pass_user_data()
    
    new_score = score_password(improved_password)

    improved_passwords = improve_password(improved_password)

    security_fields = check_security_tags(improved_password, new_score[4])

    table_name = f"{user_data['username']}_passwords"

    database_push_request(f"UPDATE {table_name} SET password_password = %s, overall_score = %s, improved_password = %s, security_fields = %s WHERE password_id = %s", (improved_password, new_score[4], str(improved_passwords), str(security_fields), password_dict_id))

    # Reload the user's data
    full_page_reload()
