# IMPORTS
from functions.database_functions.database_push_function import database_push_request
from functions.database_functions.database_create_table_function import database_create_table_request
from functions.user_info_functions.load_user_credentials import load_user_credentials
from functions.user_info_functions.load_user_passwords import load_user_passwords

def signup_process(fname, lname, email, username, password, confirmed_password):
    if password == confirmed_password: # ensures their passwords match
        try:
            database_push_request(
                "INSERT INTO users (username, user_email, user_password, user_first_name, user_last_name) VALUES (%s, %s, %s,%s, %s)", (username, email, password, fname, lname)
            ) # adds them as a record to the users table
            database_create_table_request("CREATE TABLE {0}_passwords (password_id int NOT NULL AUTO_INCREMENT, website_name varchar(255), website_url varchar(255), password_username varchar(255), password_password varchar(255), length_score int, number_score int, case_score int, symbol_score int, overall_score int, improved_password varchar(255), new_overall_score int, security_fields varchar(255), PRIMARY KEY (password_id))".format(username)) # creates their own table for storing their passwords
            load_user_credentials(username)
            load_user_passwords(username)
            return "Success"
        except:
            return "ERROR! Connection" # returned if any type of error in above code
    else:
        return "ERROR! Passwords" # returned when passwords don't match
    