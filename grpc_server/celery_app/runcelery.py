from grpc_server.app import celery, create_app
from grpc_server.celery_app import init_celery

app = create_app()
init_celery(app, celery)