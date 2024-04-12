#!/bin/bash

# Change directory to your Django project directory
cd /home/bhumika/hook

# Pull latest changes from the Git repository
git pull origin main

# Run any necessary commands to update dependencies, migrate database, etc.
python manage.py migrate
python manage.py collectstatic --noinput

# Restart the server or any necessary services
systemctl restart gunicorn.service