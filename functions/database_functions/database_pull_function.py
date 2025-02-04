# IMPORTS
import mysql.connector

def database_pull_request(sql_command, parameters): 

    # logs in to the db
    pulled_database = mysql.connector.connect(
        host="mysql-200-121.mysql.prositehosting.net",
        user="root_user",
        password="V68D,N2%JyBeqK?p~d;kW!",
        database="db_pass_secure"
    )

    # the variable that will act as a controller inside the db
    navigator = pulled_database.cursor()

    # executes the sql command and retrieves results
    navigator.execute(sql_command, parameters)
    results = navigator.fetchall()

    # returns all the results as a list
    return results