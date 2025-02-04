# IMPORTS
import requests

def fetch_compromised_passwords():
    try:
        url = "https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.txt"

        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful

        # Split the text content into a list of passwords
        compromised_passwords = response.text.splitlines()

        return compromised_passwords[8:]
    
    except requests.exceptions.RequestException as e:
        return False