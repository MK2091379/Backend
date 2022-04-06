release: python manage.py migrate
web: gunicorn automation.wsgi
worker: celery -A automation worker