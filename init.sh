#!/bin/bash
set -e

echo "Starting SSH ..."
service ssh start

# Go to directory
cd /code

gunicorn -c gunicorn.config.py app:app
# python /code/app.py