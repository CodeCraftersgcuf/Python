# auth.py
import sqlite3
import hashlib

def create_user_table():
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                     (username TEXT PRIMARY KEY, password TEXT)''')
    connection.commit()
    connection.close()

def authenticate_user(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    connection.close()

    if user:
        stored_password = user[1]
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        return stored_password == password_hash
    return False
