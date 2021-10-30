from flask_restful import Resource
from flask import request

from app.utils.http_responses import success, error

from app.core.validate import Validate
from app.celery_app.tasks import requester


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
