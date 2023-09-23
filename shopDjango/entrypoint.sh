#!/bin/sh

python manage.py migrate --noinput || exit 1
python manage.py runserver 0.0.0.0:8000
#uwsgi --harakiri=60 --master -p 8 --max-requests 100000 --disable-logging --http 0.0.0.0:9090 -b 32768 -w shopDjango.wsgi
