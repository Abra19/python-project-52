#!/usr/bin/env bash
# Exit on error
set -o errexit

# Modify this line as needed for your package manager (pip, poetry, etc.)
# poetry install
make install

# Convert static asset files
# python manage.py collectstatic --no-input
make static

# Apply any outstanding database migrations
# python manage.py migrate
make migrate