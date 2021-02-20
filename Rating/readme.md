# Introduction

The goal of this project is to provide minimalistic django Movie project template that everyone can use, which allows basic functionalities such as adding movies to the database, User comment section, Rating system. The project user custom user authentication for creation and authentication of users. different tables have been created for the comments, rating and movie section.

Template is written with django 3.1 and python 3.9 in mind.


### Main features

* Custom User Authentication.

* Bootstrap static files included.

* Separated requirements files.

* SQLite3 by default if no env variable is set.

* User Comment section is provided.

* Seperate error handler templates have been provided.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/gocardless/sample-django-app.git
$ cd sample-django-app
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python -m venv env_name
$ env_name/Scripts/activate
```

Then install the dependencies:

```sh
(env_name)$ pip install -r requirements.txt
```
Note the `(env_name)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `venv`.

Once `pip` has finished downloading the dependencies make migrations to apply changes to the database:

```sh
(env_name)$ cd project
(env_name)$ python manage.py migrate
```

Once the migrations has finished createsuperuser to access the application:

```sh
(env_name)$ python manage.py createsuperuser
```
and enter the details as per your choice.

Once done with the steps above run the development server using the command:

```sh
(env_name)$ python manage.py runserver
```

And navigate to `http://127.0.0.1:8000/`. Login with the credentials you entered while creating superuser.
