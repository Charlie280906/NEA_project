# IMPORTS
from functions.database_functions.database_pull_function import database_pull_request
from functions.user_info_functions.load_user_credentials import load_user_credentials
from functions.user_info_functions.load_user_passwords import load_user_passwords

def login_authentication(username, password):
    
    # pulls only email and password field of users
    credentials = database_pull_request("SELECT username, user_password FROM users", ())

    # compares the tuple of the entered fields to db tuples
    if (username, password) in credentials:
        load_user_credentials(username)
        load_user_passwords(username)
        return True
    else:
        return False
