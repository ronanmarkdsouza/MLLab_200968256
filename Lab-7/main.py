# Importing Libraries
from sqlalchemy import false, true
import streamlit as st
import hashlib
import pandas as pd
import sqlite3

page_flag = 0
lgoin_flag = false
# Connecting to local SQLite3 Database for Testing
conn = sqlite3.connect(database='data.db')
c = conn.cursor()

# Function to Hash Passwords
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

# Function to check the hashes of the password from the Database
def check_hashes(password,hashed_text):
	if make_hashes(password) == hashed_text:
		return hashed_text
	return False

# Function to Create the User Table in the database
def create_usertable():
	c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT PRIMARY KEY UNIQUE,password TEXT)')

# Function to add User data to the Database
def add_userdata(username,password):
	c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

# Function for login of the user
def login_user(username,password):
	c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = c.fetchall()
	return data

# Function to view all users on the Database
def view_all_users():
	c.execute('SELECT * FROM userstable')
	data = c.fetchall()
	return data

# Main Function
def main():
    st.title("Lmao")
    st.write("This is the main function kuch likh lol")


if __name__ == '__main__':
    main()