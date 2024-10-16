import mysql.connector

try:
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='mysql12345',
        # db='django_crm',
        # auth_plugin='caching_sha2_password'
    )
    print("DB Connection successful!")
    cursorObject = connection.cursor()
    cursorObject.execute("CREATE DATABASE django_crm")
    print("Database created")
except mysql.connector.Error as err:
    print(f"Error: {err}")