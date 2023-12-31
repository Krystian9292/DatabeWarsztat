from psycopg2 import connect, OperationalError
from psycopg2.errors import DuplicateTable, DuplicateDatabase

Create_db = "CREATE DATABASE workshop;"

Create_tb = """CREATE TABLE users(
    id serial PRIMARY KEY,
    username varchar(255) UNIQUE,
    hashed_password varchar(80)
)"""

Create_tb1 = """CREATE TABLE messages(
    id serial PRIMARY KEY,
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    creation_date TIMESTAMP,
    text varchar(255)
)"""

DB_USER = "postgres"
DB_PASSWORD = "coderslab"
DB_HOST = "127.0.0.1"

try:
    cnx = connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()

    try:
        cursor.execute(Create_db)
        print("Database created")

    except DuplicateDatabase as e:
        print("Database exists ", e)

    cnx.close()

except OperationalError as e:
    print("Connection Error: ", e)



try:
    cnx = connect(database="workshop", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()


    try:
        cursor.execute(Create_tb)
        print("Table users created")

    except DuplicateTable as e:
        print("Table exists ", e)


    try:
        cursor.execute(Create_tb1)
        print("Table messages created")

    except DuplicateTable as e:
        print("Table exists ", e)
    cnx.close()

except OperationalError as e:
    print("Connection Error: ", e)