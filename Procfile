web:       gunicorn cabot.wsgi --log-file -
celery:    celery worker -A cabot --loglevel=INFO --concurrency=3 -Ofair
beat:      celery beat -A cabot --loglevel=INFO
