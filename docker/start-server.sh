#!/bin/bash
if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] ; then
    (cd backend; python manage.py migrate; python manage.py createsuperuser --no-input;  python manage.py collectstatic --noinput)
else 
    (cd backend; python manage.py migrate; python manage.py collectstatic --noinput)
fi
chmod -R 777 backend/logs
chmod -R 777 backend/static
(cd backend; gunicorn immfly.wsgi --user www-data --bind 0.0.0.0:8000 --workers 3 --reload) & nginx -g "daemon off;"
