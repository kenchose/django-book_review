# Belp - Book review app

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Prerequisites](#prerequisites)
* [Setup](#setup)

## General info
Belp is a CRUD web application allowing users to add a new books, images, add comments, and give a 1-5 star rating and share it to everyone. Only the user can delete or edit their own review, messages, and profile. Each book that a user has done a review on will show on their user profile page. 

## Technologies
* Bcrypt version:3.1.4
* Python version: 2.7.10
* MySQL version: 14.14
* Django version: 1.10
* Bootstrap version: 4.3.1

## Prerequisites

What things you need to install the software and how to install them
```
$ brew update
$ brew install python
$ pip install
Mac/Linux: $ pip install virtualenv
Windows: $ python -m install virtualenv
$ virtualenv djangoEnv
```
## Setup
* Clone this repo to your local machine using `https://github.com/kenchose/django-book_review.git`
To run this project, install it locally using pip:
```
$ ../djangoEnv
$ source djangoEnv/bin/activate
$ pip install Django==1.10
$ pip install bcrypt
```
* Go to the root of the project and run `python manage.py runserver`
