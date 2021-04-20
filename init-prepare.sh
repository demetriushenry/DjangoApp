#!/bin/sh
rm -r gateway/migrations/*
python manage.py migrate --noinput
python manage.py collectstatic --no-input --clear
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'Admin123')" | python manage.py shell

exec "$@"