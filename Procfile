release: python manage.py tailwind install && python manage.py tailwind build && python manage.py collectstatic --noinput && python manage.py migrate
web: gunicorn core.wsgi:application 