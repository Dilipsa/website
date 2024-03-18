"""
MVT architecture
M => Model          --> database layer
V => View           --> business logic / backend layer
T => Template       --> frontend layer

Steps:
=================
1] Create a folder which is going to be my django project ex: mysite
2] Open this folder in yout text editor i.e VS code
3] Similarly open you folder in cmd.
4] Installing virtualenv this is one time task
  command:
    pip install virtualenv
5] Creating a virtualenv
  command:
    python -m venv venv
6] Activating virtualenv
  command:
    venv\Scripts\activate
7] installing django
  command:
    pip install django           => install latest version of django
    pip install django==2.2.15   => install specified djagno version
8] Create a django project
  command:
    django-admin startproject mysite   => creating a django project inside the folder
    django-admin startproject mysite . => makes parent folder as a django project
9] Running the development server:
  command:
    python manage.py runserver
"""
