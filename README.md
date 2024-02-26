### Hexlet tests and linter status, Maintability:
[![Actions Status](https://github.com/Abra19/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Abra19/python-project-52/actions)
[![Python CI](https://github.com/Abra19/page_analyzer/actions/workflows/python_ci.yml/badge.svg)](https://github.com/Abra19/page_analyzer/actions/workflows/python_ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/e08d3f09e7d1220cad9b/maintainability)](https://codeclimate.com/github/Abra19/python-project-52/maintainability)


### Descriptions
This project built with Python and Django framework and implements a task management system that allows you to set tasks, assign executors and change their statuses. Registration and authentication are required to work with the system.

The frontend is rendered on the backend using the Bootstrap framework. Pages are built by the DjangoTemplates backend.

As the object-relational database system we are using PostgreSQL.

### Requirements
1. Python >=3.10
2. poetry >= 1.2.0
3. django >= 5.0.2
4. django-bootstrap5 >= 23.4
5. postgreSQL >= 16
5. gunicorn >= 21.2.0


### To get started
1. Clone git repo:
  `git@github.com:Abra19/python-project-52.git`
2. Go to directory python-project-52:
  `cd python-project-52`
3.  Configuring `poetry` to create a virtual environment:
  `poetry config virtualenvs.in-project true`
4.  Create virtual environment and Install dependencies
  `make install`
5. Create `.env` file in the root folder similar to `.env.example`
5. Start app
  `make migrate`
  `make start`

### [Try the application](https://python-project-52-gbo3.onrender.com)