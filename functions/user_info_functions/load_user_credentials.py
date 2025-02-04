# IMPORTS
from functions.database_functions.database_pull_function import database_pull_request
import json
import rsa

# Function to load user credentials from a database and update a JSON file
def load_user_credentials(username):
    # Pull user data from the database using their username
    data = database_pull_request("SELECT * FROM users WHERE username = %s;", (username,))
    
    with open("json/full_user_info.json", "r") as file:
        # Load the JSON contents into Python
        contents = json.load(file)
    
    # Generate keys and serialize them
    publicKey, privateKey = rsa.newkeys(512)
    publicKeyPem = publicKey.save_pkcs1().decode("utf-8")
    privateKeyPem = privateKey.save_pkcs1().decode("utf-8")

    key_pair = {"publicKey": publicKeyPem, "privateKey": privateKeyPem}

    # Updates fields in the JSON file
    contents["username"] = data[0][1]
    contents["user_email"] = data[0][2]
    contents["user_password"] = data[0][3]
    contents["user_first_name"] = data[0][4]
    contents["user_last_name"] = data[0][5]
    contents["encryption_keys"] = key_pair

    with open("json/full_user_info.json", "w") as file:
        # 'indent=4' ensures the JSON is formatted in a readable way
        json.dump(contents, file, indent=4)