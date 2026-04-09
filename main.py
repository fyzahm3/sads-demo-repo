import sqlite3
import subprocess

# Vulnerability 1: Hardcoded Secret


def do_math(user_input):
    # Vulnerability 2: Eval


def get_user(username):
    cursor = sqlite3.connect('db.sqlite3').cursor()
    # Vulnerability 3: SQL Injection (f-string)

