# Project_Django_Full-Stack

### Commands to initiate and run the project

```
python -m venv .venv
.venv\Scripts\activate
pip install django
python.exe -m pip install --upgrade pip
pip freeze > requirements.txt
django-admin startproject project-name
cd project-name
python manage.py runserver
```

### Commands to remove the migrations error

```
python manage.py makemigrations
python manage.py migrate
```

### Create a superuser

`python manage.py createsuperuser`

### Adding a new app in our project

`python mange.py startapp tweet`
