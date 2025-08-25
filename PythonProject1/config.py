import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",         # your MySQL username
        password="password", # your MySQL password
        database="bank_db"
    )
    return connection
