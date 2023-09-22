# registration.py
import sqlite3
import hashlib

def register_user(username, password):
    connection = sqlite3.connect("users.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        connection.close()
        return "Username already exists. Please choose another one."

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("INSERT INTO users VALUES (?, ?)", (username, password_hash))
    connection.commit()
    connection.close()
    return "Registration successful."
