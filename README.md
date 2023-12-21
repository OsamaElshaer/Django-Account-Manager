# Django User Authentication and Profile Management

This Django project focuses on enhancing user authentication and profile management by substituting the default User model with `AbstractUser`, implementing user profiles, and providing a easy authentication process. The project also includes signals for automatic profile creation upon user registration.

## Project Status

This project has been completed.

## About The Project

Built using **Django** as the backend framework, this project use the power of Django to allowing developers to focus on app logic. The database is powered by SQLite.

## Installation

1. Clone the repo
2. vertual enviroment
    ```sh
     python -m venv env
     env\scripts\activate
    ```
3. install requirements
    ```sh
     pip install -r requirements.txt
    ```
4. migrate --> create user admin
    ```sh
     python manage.py migrate
     python manage.py createsuperuser
    ```
5. run server
    ```sh
     python manage.py runserver
    ```
