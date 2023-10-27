Create_db = "CREATE DATABASE workshop;"

Create_tb = """CREATE TABLE users(
    id serial PRIMARY KEY,
    username varchar(255) UNIQUE,
    hashed_password varchar(80)
)"""

Create_tb1 = """CREATE TABLE messages(
    id serial PRIMARY KEY,
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES user(id) ON DELETE CASCADE
    creation_date timestamp,
    text varchar(255)
)"""