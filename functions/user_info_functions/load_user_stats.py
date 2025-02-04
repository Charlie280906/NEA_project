# IMPORTS
from functions.user_info_functions.pass_user_data import pass_user_data
import json


def load_user_stats():
    user_data = pass_user_data()

    user_stats = {
        "total": 0,
        "weak": 0,
        "reused": 0,
        "at_risk": 0,
        "average": 0
    }

    total = len(user_data["user_passwords"])
    user_stats["total"] = total

    weak = 0
    for password in user_data["user_passwords"]:
        if "weak" in password["security_fields"]:
            weak += 1
    user_stats["weak"] = weak

    reused = 0
    for password in user_data["user_passwords"]:
        if "reused" in password["security_fields"]:
            reused += 1
    user_stats["reused"] = reused

    at_risk = 0
    for password in user_data["user_passwords"]:
        if "compromised" in password["security_fields"]:
            at_risk += 1
    user_stats["compromised"] = at_risk

    score = []
    for password in user_data["user_passwords"]:
        score.append(password["overall_score"])
    try:
        average = int(sum(score)/total)
    except:
        average = 0
    user_stats["average"] = average

    with open("json/full_user_info.json", "r") as file:
        data = json.load(file)

    # Update the "user_stats" field
    data["user_stats"] = user_stats

    with open("json/full_user_info.json", "w") as file:
        json.dump(data, file, indent=4)