1. Create a project folder-
   - mkdir <project_folder_name>
3. Create a virtual environment using python -
  - python3 -m venv <env_name>
4. Activate virtual environment-
   - source env/bin/activate
5. Install module registered in requirements.txt via pip-
   - pip install -r requirements.txt
6. Create django project-
   - django-admin startproject <project_name>
7. Goto inside project folder-
  - cd <project_name>
8. Create django app-
  - python manage.py startapp <app_name>
9. Register your app in your django project's settings.py inside INSTALLED_APPS-
  - INSTALLED_APPS[...,<app_name>,]
10. Store openAI creds in .env file.
11. Add models as per project requirements in django_app/models.py-
  - Conversation, Message
12. After that migrate db-
  - python manage.py makemigrations
  - python manage.py migrate
13. Run the server-
  - python manage.py runserver
14. Create superuser/admin-
  - python manage.py createsuperuser


** Basic server start at localhost:8000 **
