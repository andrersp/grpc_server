from flask import Blueprint
from flask_restful import Api
from app.blueprints.rest_v1.retrieve import Retrieve

bp = Blueprint("rest_v1", __name__, url_prefix="/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(Retrieve, "/movies")
    app.register_blueprint(bp)
