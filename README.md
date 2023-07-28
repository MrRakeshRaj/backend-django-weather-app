# Django Weather APP
Django Backend to provide weather forecast data



## Spin Up the Project

- Clone the template project to your local:
```git
https://github.com/MrRakeshRaj/backend-django-weather-app.git
```

- Use the folder created after clone as the project main directory, cd to this new directory.
- use pipenv (mac) which is a dependency management tool
  

- Create virtual environment as a best practice:
```py
python3 -m venv env # for Windows or
python -m venv env # for Windows
virtualenv env # for Mac/Linux or;
virtualenv env -p python3 # for Mac/Linux
```

- Activate scripts:
```bash
.\env\Scripts\activate  # for Windows
source env/bin/activate  # for MAC/Linux
```

- See the (env) sign before your terminal.

- Install dependencies:
```py
pip install -r requirements.txt
```

## Secure your project

### .gitignore

A standard .gitignore file has already added to the project root directory. 

### python-decouple

- Create .env file on root directory. We will collect our variables in this file.
```
API_KEY=<your API Key from open wether api>
```

- Migrate:
```bash
python3 manage.py migrate  # or;
python manage.py migrate  # or;
py manage.py migrate
```

- Create superuser:
```bash
py manage.py createsuperuser  # or;
python manage.py createsuperuser  # or;
python3 manage.py createsuperuser
```

- Delete .git folder.

- From now on you can send your project to the github.

- Run the server and see the initial setup:
```bash
py manage.py runserver  # or;
python manage.py runserver  # or;
python3 manage.py runserver
