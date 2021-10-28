from flask import Flask
from .ext import config

from celery import Celery

celery = Celery('grpc_server', config_source='grpc_server.celery_app.celeryconfig')


def minimal_app():
    app = Flask(__name__)
    return app


def create_app():
    app = minimal_app()
    config.init_app(app)
    config.load_extensions(app)
    return app