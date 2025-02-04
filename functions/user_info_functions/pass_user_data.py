# IMPORTS
import json

# Function to get the user data from the JSON file and pass to script
def pass_user_data():
    with open("json/full_user_info.json", "r") as file:
        contents = json.load(file)

    return contents