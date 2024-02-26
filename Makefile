install:
	poetry install

lint:
	poetry run flake8 task_manager

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

dev: migrate
	poetry run python manage.py runserver

build:
	poetry build

PHONY: install lint migrate dev build