def score_password(password):
    length_score = 0
    number_score = 0
    case_score = 0
    symbol_score = 0
    overall_score = 0

    if len(password) >= 12:
        length_score += 25
    else:
        length_score += ((len(password)/12)*25)

    number_count = 0
    for number in range (0, 10):
        number_count += password.count(str(number))
    if number_count >= 3:
        number_score += 25
    else:
        number_score += ((number_count/3)*25)

    lowercase_count = 0
    uppercase_count = 0
    for character in password:
        if character.islower():
            lowercase_count += 1
        if character.isupper():
            uppercase_count += 1
    try:
        if lowercase_count/uppercase_count >=0.5 and lowercase_count/uppercase_count <= 1.5:
            case_score += 25         
        elif lowercase_count > uppercase_count:
            case_score += ((uppercase_count/lowercase_count)*25)
        else:
            case_score += ((lowercase_count/uppercase_count)*25)
    except:
        case_score = 0

    symbol_count = 0
    special_characters = "[@_!#$%^&*()<>?/\|}{~:]£"
    for character in password:
        if character in special_characters:
            symbol_count += 1
    if symbol_count >= 3:
        symbol_score += 25
    else:
        symbol_score += ((symbol_count/25)*100)

    overall_score += length_score + number_score + case_score + symbol_score

    return [int(length_score), int(number_score), int(case_score), int(symbol_score), int(overall_score)]