# # Use of eval
user_input = input("Enter your command: ")
eval(user_input)

###############################################################################

user_input = "os.system('ls')"  # Imagine this is input from a user
exec(user_input)

###############################################################################

import pickle
# Dangerous if `data` comes from an untrusted source
data = pickle.loads(some_input)

###############################################################################

from subprocess import run
command = input("Enter a command: ")  # Unsafe user input
run(command, shell=True)

###############################################################################

import os
command = input("Enter a command: ")  # Unsafe user input
os.system(command)

###############################################################################

file_path = input("Enter the file path to open: ")  # Unsafe user input
with open(file_path, 'r') as file:
    print(file.read())

###############################################################################

module_name = input("Enter the module name to import: ")  # Unsafe user input
__import__(module_name)

###############################################################################

# Example of a hard-coded password
password = "SuperSecretPassword123!"

###############################################################################

import sqlite3

# SQL injection vulnerability
user_input = "user_input; DROP TABLE users;"
conn = sqlite3.connect('example.db')
c = conn.cursor()
c.execute(f"SELECT * FROM users WHERE name = '{user_input}'")
