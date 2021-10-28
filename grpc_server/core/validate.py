from grpc_server.utils.schemas.retrieve import RetrieveSchema
from marshmallow.exceptions import ValidationError


class Validate(object):

    def validate(self, data):
        try:
            data = RetrieveSchema().load(data)
        except ValidationError as e:
            raise ValidationError(e.messages)
        return data
