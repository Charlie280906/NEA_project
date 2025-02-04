# IMPORTS
from functions.database_functions.database_pull_function import database_pull_request
import json

# Function to load a user's password records from the database and update a JSON file
def load_user_passwords(username):
    table_name = f"{username}_passwords"
    data = database_pull_request(f"SELECT * FROM `{table_name}`;", ())
    
    with open("json/full_user_info.json", "r") as file:
        # Load the JSON data into Python
        contents = json.load(file)

    contents["user_passwords"] = []
    
    for row in data:
        # Creates a template for the records
        record = {
            "password_id": None,
            "website_name": None,
            "website_url": None,
            "password_username": None,
            "password_password": None, #4
            "length_score": None,
            "number_score": None,
            "case_score": None,
            "symbol_score": None,
            "overall_score": None,
            "improved_password": None,
            "new_overall_score": None,
            "security_fields": None,
        }
        
        # Get all keys in the record as a list
        keys = record.keys()
        
        for i in range(0, 13):
            if i == 4:
                record[list(keys)[i]] = row[i]
            else:
                record[list(keys)[i]] = row[i]  # Assigns each value in the record one matching from the database
    
        contents["user_passwords"].append(record)
    
    with open("json/full_user_info.json", "w") as file:
        # 'indent=4' ensures the JSON is formatted in a readable way
        json.dump(contents, file, indent=4)
