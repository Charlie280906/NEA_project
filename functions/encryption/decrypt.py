# IMPORTS
from functions.user_info_functions.pass_user_data import pass_user_data
import rsa

def decrypt(data):
    try:
        # Required to gain the encryption keys from the JSON file
        user_data = pass_user_data()
        privateKeyPem = user_data["encryption_keys"]["privateKey"]

        # Convert string back to Python object
        privateKey = rsa.PrivateKey.load_pkcs1(privateKeyPem.encode("utf-8"))

        # Decrypt the message using the private key
        decMessage = rsa.decrypt(data, privateKey).decode()

        return decMessage
    except:
        return False