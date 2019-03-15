{% if False %}

# Introduction

The goal of this project is to learn how to work with models, relation between them and to send and retrieve data from and to the template. 

Template is written with django 2.1.5 and python 3 in mind.

### Main features

* Extended User model

* User inscription in sports

* data seeds for easy tests

* SQLite database

# Usage

To use this project:

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
      
      
After that just run migrations, and start the server.

{% endif %}

# Club Sport

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/fakham/django_club_sport.git django_club_sport
    $ cd django_club_sport
    
Activate the virtualenv for your project.
    
    
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver