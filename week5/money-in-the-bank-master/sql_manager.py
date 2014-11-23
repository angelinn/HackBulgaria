import requests
import sqlite3
import hashlib
from Client import Client
from datetime import datetime

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def create_clients_table():
    create_query = '''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                password_failures INTEGER DEFAULT 0,
                password_failure_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP)'''

    cursor.execute(create_query)


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    if is_password_valid(new_pass) is False:
        return False

    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (hashlib.md5(new_pass.encode()).hexdigest(), logged_user.get_id()))
    conn.commit()


def register(username, password):
    if is_password_valid(password) is False:
        return False

    insert_sql = "insert into clients (username, password) values (?, ?)"
    cursor.execute(insert_sql, (username, hashlib.md5(password.encode()).hexdigest()))
    conn.commit()
    return True


def is_password_valid(password):
    if len(password) < 8:
        return False

    lower_flag = False
    upper_flag = False
    special_flag = False
    number_flag = False

    special_characters = '!?@#$%^&*()_+-=.,:;/\\()[]'

    for char in password:
        if char == chr(ord(char) & 0xDF):
            upper_flag = True
        if char == chr(ord(char) | 0x20):
            lower_flag = True
        if char <= '9' and char >= '0':
            number_flag = True
        if special_characters.find(char) != -1:
            special_flag = True

    if lower_flag is False or upper_flag is False or special_flag is False or number_flag is False:
        return False

    return True


def login(username, password):
    select_query = """SELECT id, username, balance, message
                      FROM clients
                      WHERE username = ? AND password = ?
                      LIMIT 1"""

    failure_details = cursor.execute('''SELECT password_failures, password_failure_time
                                        FROM clients
                                        WHERE username = ?
                                        LIMIT 1''', (username, )).fetchone()
    failures = 0

    if failure_details:
        failures = failure_details[0]
        time_failed = failure_details[1]
        print(time_failed)
        time_left = (datetime.now() - time_failed).total_seconds()

        if failures >= 5 and time_left < 300:
            print("You have enter wrong password too many times!\nPlease wait another {} minute(s)"
                  .format(time_left / 60))
            return False

    cursor.execute(select_query, (username, hashlib.md5(password.encode()).hexdigest()))
    user = cursor.fetchone()

    if(user):
        cursor.execute('''UPDATE clients
                          SET password_failures = 0
                          WHERE username = ?''', (username, ))
        conn.commit()

        return Client(user[0], user[1], user[2], user[3])
    else:
        if failures < 5:
            cursor.execute('''UPDATE clients
                              SET password_failures = ?
                              WHERE username = ?''', (failures + 1, username))
            conn.commit()

        return False
