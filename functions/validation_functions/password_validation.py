def validate_password(data):
    if " " in data:
        return False
    else:
        return data