#!/usr/bin/env sh
# exit on error

set -o errexit

pip install -r ./requirements/requirements.txt
python manage.py collectstatic --no-input
