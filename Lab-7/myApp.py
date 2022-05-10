import streamlit as st
import pandas as pd
import numpy as np
import sqlite3
import hashlib
import streamlit.components.v1 as components

con = sqlite3.connect('data.db')
cur = con.cursor()

def main():
    st.title("Movie Recommendation System")
    menu = ["Home", "Sign-Up", "Login"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        home()

    elif choice == "Sign-Up":
        signup()

    elif choice == "Login":
        login()

def signup():
    st.title("Sign-Up Page")
    st.write("This will have the sign-up for the app")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    st.write("Terms and Conditions: ")
    agree = st.checkbox("I Agree")
    st.button("Sign-Up")

def login():
    st.title("Login Page")
    st.write("This will be the login page for the app")
    username = st.text_input("Username")
    password = st.text_input("Password", type='password')
    st.button("Login")

def home():
    st.title("Home Page")
    st.write("This is the home page which will have the movie recommendations and search bar")
    search_text = st.text_input("Search")
    st.button("Search")

if __name__ == "__main__":
    main()