#!/bin/bash

# Change directory to your Django project directory
cd /home/bhumika/Tourr_up

# Pull latest changes from the Git repository
git pull origin main

# Run any necessary commands to update dependencies, migrate database, etc.
python3 manage.py migrate
# python3 manage.py collectstatic --noinput

# Restart the server or any necessary services
# python3 manage.py runserver