# IMPORTS
import pandas as pd

def password_company_creator():
    # Load the dataset (downloaded as a CSV file)
    data = pd.read_csv("functions/entry_functions/fortune1000_2023.csv")

    # Assuming the company names are in a column named 'Company'
    password_company_options = list(data["Company"].tolist())

    password_company_options.sort()

    password_company_options.append("Add another option...")

    password_company_options = tuple(password_company_options)

    return password_company_options