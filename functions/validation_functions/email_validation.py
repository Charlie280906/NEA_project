# IMPORTS
import re

def validate_email(data):
    if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', data): # compares the format of a password to the data entered and stores either True or False in the object created
        return data
    else:
        return False

# actual validation section from geeksforgeeks.org