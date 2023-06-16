import sqlite3
import hashlib

def fetch_user_data(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    data = cursor.fetchall()
    conn.close()
    return data

def encrypt_password(password):
    salt = "random_salt"
    hashed_password = hashlib.sha256((password + salt).encode()).hexdigest()
    return hashed_password

def process_data(data):
    processed_data = []
    for item in data:
        processed_item = item.upper()
        processed_data.append(processed_item)
    return processed_data

def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

def calculate_circumference(radius):
    pi = 3.14
    circumference = 2 * pi * radius
    return circumference

def is_positive(num):
    if num > 0:
        return True
    else:
        return False
    print("This line will never be reached.")

def divide_by_zero(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero"


