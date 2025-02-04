# IMPORTS
import mysql.connector

def database_create_table_request(sql_command):

    # logs in to the db
    pushing_to_database = mysql.connector.connect(
        host="mysql-200-121.mysql.prositehosting.net",
        user="root_user",
        password="V68D,N2%JyBeqK?p~d;kW!",
        database="db_pass_secure"
    )

    # the variable that will act as a controller inside the db
    navigator = pushing_to_database.cursor()

    # example of 'sql_command' --> "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))"
    navigator.execute(sql_command)