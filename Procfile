release: chmod +x build.sh && ./build.sh
web: gunicorn core.wsgi:application --bind 0.0.0.0:$PORT 