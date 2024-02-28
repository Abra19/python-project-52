PORT ?= 8000

install:
	poetry install

lint:
	poetry run flake8 task_manager

collect_ru:
	poetry run django-admin makemessages -l ru

collect_en:
	poetry run django-admin makemessages -l en

compile_texts:
	poetry run django-admin compilemessages

static:
	poetry run python manage.py collectstatic --noinput

createsuperuser:
	poetry run python manage.py createsuper

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

dev: migrate
	poetry run python manage.py runserver

start:
	poetry run gunicorn -w 5 -b 0.0.0.0:$(PORT) task_manager.wsgi

PHONY: install lint static migrate dev start