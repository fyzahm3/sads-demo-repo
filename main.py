import sqlite3
import subprocess

# Vulnerability 1: Hardcoded Secret
password = "super_secret_123"

def do_math(user_input):
    # Vulnerability 2: Eval
    return eval(user_input)

def get_user(username):
    cursor = sqlite3.connect('db.sqlite3').cursor()
    # Vulnerability 3: SQL Injection (f-string)
    cursor.execute(f"SELECT * FROM users WHERE name = '{username}'")
