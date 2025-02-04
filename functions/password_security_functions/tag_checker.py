from functions.user_info_functions.pass_user_data import pass_user_data
from functions.compromisation_functions.compromised_getter import fetch_compromised_passwords

def check_security_tags(password, overall_password_score):

    user_data = pass_user_data()

    security_fields = []

    if overall_password_score < 75:
        security_fields.append("weak")

    for password_group in user_data["user_passwords"]:
        if password_group["password_password"] == password and "reused" not in security_fields:
            security_fields.append("reused")

    compromised_passwords = fetch_compromised_passwords()
    if password in compromised_passwords:
            security_fields.append("compromised")

    return security_fields



