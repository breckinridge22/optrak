#!/bin/bash
python /project/optrak/manage.py makemigrations
python /project/optrak/manage.py migrate
python /project/optrak/manage.py runserver 0.0.0.0:8000