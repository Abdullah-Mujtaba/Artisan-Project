web: python manage.py migrate && python manage.py collectstatic --noinput && python -m gunicorn artisan.wsgi --bind 0.0.0.0:$PORT
