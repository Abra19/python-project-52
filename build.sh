#!/usr/bin/env bash
# Exit on error
set -o errexit

make install

# Convert static asset files
make static

# Create superuser for admin page
make createsuperuser

# Apply any outstanding database migrations
make migrate