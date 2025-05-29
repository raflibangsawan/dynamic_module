#!/bin/bash

# Create theme app
python manage.py startapp theme

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