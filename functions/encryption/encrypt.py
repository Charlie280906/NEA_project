# IMPORTS
from functions.user_info_functions.pass_user_data import pass_user_data
import rsa


# TODO: acc include these when sending to db
def encrypt(data):
    # Required to gain the encryption keys from the JSON file
    user_data = pass_user_data()
    publicKeyPem = user_data["encryption_keys"]["publicKey"]

    # Convert string back to Python object
    publicKey = rsa.PublicKey.load_pkcs1(publicKeyPem.encode("utf-8"))

    # Encrypt the message using the public key
    encMessage = rsa.encrypt(data.encode(), publicKey)

    return encMessage

