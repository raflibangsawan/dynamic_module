#!/bin/bash

# Create theme directory if it doesn't exist
mkdir -p theme

# Create __init__.py in theme directory
touch theme/__init__.py

# Initialize tailwind
python manage.py tailwind init theme

# Install tailwind dependencies
python manage.py tailwind install

# Build tailwind
python manage.py tailwind build

# Collect static files
python manage.py collectstatic --noinput

# Run migrations
python manage.py migrate 