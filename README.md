﻿## Register-login-Project
Project Description
This project is a Register and Login System built using Django, designed to provide a secure authentication mechanism for users. It includes user registration, login, logout, and authentication handling. The project follows Django’s best practices for user authentication and security.

## Features  
 User Registration – New users can sign up with a username, email, and password.
 Secure Authentication – Users can log in securely using Django’s authentication system.
 Password Hashing – User passwords are securely stored using Django’s built-in hashing mechanism.
 Logout Functionality – Users can log out safely.
 Form Validation – Checks for valid input and prevents duplicate usernames.
 
## Technologies Used in this Project
Backend: Django (Python)
Frontend: HTML, CSS, Bootstrap
Database: MySql 
Version Control: Git & GitHub

## Installation & Setup
Follow these steps to set up and run the project on your local machine:
Clone the Repository
git clone https://github.com/Akshay-Kumar-97/Register-login-Project.git
cd Register-login-Project

## Create & Activate Virtual Environment (Recommended)
python -m venv env
source env/bin/activate    # On macOS/Linux
env\Scripts\activate       # On Windows

## Install Dependencies
pip install -r requirements.txt

## Run Database Migrations
python manage.py migrate

## Start the Development Server
python manage.py runserver
Now open your browser and visit http://127.0.0.1:8000/ to access the application.
