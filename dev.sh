#!/bin/bash

# Start Tailwind CSS in watch mode
npx tailwindcss -i ./static/css/main.css -o ./static/css/output.css --watch &

# Start Django development server
python manage.py runserver

# Kill the Tailwind process when Django server stops
trap "kill $!" EXIT 