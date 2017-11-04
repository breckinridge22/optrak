#!/bin/bash
python3 /project/optrak/manage.py makemigrations
python3 /project/optrak/manage.py migrate
python3 /project/optrak/manage.py runserver 0.0.0.0:8000