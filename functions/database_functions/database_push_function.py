# IMPORTS
import mysql.connector

def database_push_request(sql_command, values):

    # logs in to the db
    pushing_to_database = mysql.connector.connect(
        host="mysql-200-121.mysql.prositehosting.net",
        user="root_user",
        password="V68D,N2%JyBeqK?p~d;kW!",
        database="db_pass_secure"
    )

    # the variable that will act as a controller inside the db
    navigator = pushing_to_database.cursor()

    # example of 'sql_command' --> "INSERT INTO customers (name, address) VALUES (%s, %s)"
    # example of 'values' --> ("John", "Highway 21")
    navigator.execute(sql_command, values)

    # adds to db
    pushing_to_database.commit()