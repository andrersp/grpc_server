from flask_restful import Resource
from flask import request

from grpc_server.utils.http_responses import success, error

from grpc_server.core.validate import Validate
from grpc_server.celery_app.tasks import requester


# Fix: Usar Exception do projeto
from marshmallow.exceptions import ValidationError


class Retrieve(Resource):
    def post(self):
        data = request.json

        try:
            data = Validate().validate(data)

        except ValidationError as e:
            return error(e.messages)

        else:
            requester.request.delay(data)

        return success(status_code=201)
