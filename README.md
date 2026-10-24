# Steps to create a Django Project

1. Create a fonlder for the new project
2. Open VS Code and a terminal at the that project (or any other IDE)
3. Create the virtual enviroment
    - Mac: python3 -m venv venv
4. Activate the venv
    - Mac: source venv/bin/activate
5. Install the required dependencie
    - Mac: pip3 install django
6. Create the django project (One time only command)
    *** don't forget the " . " at the end
    - Mac: django-admin startproject NAME_FOLDER .
    Ecpectation is: NAME_FOLDER folder, venv folder and manage.py
7. Update settings.py to recognize **static** and **templates** folders
    Expectation is: templates and static folders are created
    7.1. Inside of static you can create three subfolders called: js, images and css
8. Adding misc files: .gitignore, README.md
9. To generate the requirements.txt file:
    - Mac: pip3 freeze > requirements.txt# blog-112

## Django Subcomands
1. To create a django app:
    -Mac: python3 manage.py startapp APP_NAME

2. To verify if we have issues/errors:
    Mac: python3 manage.py check

3. To create an admin user:
    Mac: python3 manage.py createsuperuser
    this will ask you for a username, email, password and password confirmation

4. To detect changes and create migrations files (MODELS):
    - Both OS: python manage.py makemigrations

5. To execute changes against the db:
    - Both OS: python manage.py migrate

6. To run the server:
    - Both OS: python manage.py runserver