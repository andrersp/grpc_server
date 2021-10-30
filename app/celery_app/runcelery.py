from app.app import celery, create_app
from app.celery_app import init_celery

app = create_app()
init_celery(app, celery)
