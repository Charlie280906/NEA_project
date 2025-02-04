def validate_string(data):
    try: 
        if data.isalpha():
            return data
        else:
            return False
    except:
        return False