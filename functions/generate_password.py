# IMPORTS
from random import choice
from functions.password_security_functions.password_scorer import score_password

def generate_password(length_criteria, upper_case_criteria, lower_case_criteria, numbers_criteria, special_characters_criteria):
    
    password = []

    character_groups = {
        "upper_case" : ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"],
        "lower_case" : ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        "numbers" : ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
        "special_characters" : ["!", "@", "£", "$", "#", "€", "%", "^", "&", "*", "(", ")", "<", ">", ":", ";", ",", ".", "?", "/", "-", "+", "+"]
    }

    while len(password) < length_criteria:
        character_selection_options = list(character_groups.keys())
        character_choice = choice(character_selection_options)

        if locals()[character_choice+"_criteria"] == True:
            selected_character_list = character_groups[character_choice]
            password.append(choice(selected_character_list))

    return (["".join(password), score_password("".join(password))])