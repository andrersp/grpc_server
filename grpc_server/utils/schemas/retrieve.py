# -*- coding: utf-8 -*-

from marshmallow import Schema, fields, ValidationError, INCLUDE, validate
from marshmallow.validate import OneOf, URL
from pycpfcnpj import cpfcnpj
import re


class ClearRegister(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return "".join(re.findall(r'[0-9]', value))

    def _deserialize(self, value, attr, data, **kwargs):
        value = "".join(re.findall(r'[0-9]', value))
        value = value.zfill(11) if len(value) <= 11 else value.zfill(14)
        if not cpfcnpj.validate(value):
            raise ValidationError("Register number not valid")
        return value


class ClearProvince(fields.Field):
    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return ""
        return "".join(re.findall(r'[0-9]', value))

    def _deserialize(self, value, attr, data, **kwargs):

        value = [x for x in value if x]

        for x in value:
            if not re.match(r"^[A-Z]{2}$", x):
                raise ValidationError("Provinde dont match")

        return value


class ClearList(fields.Field):

    def _serialize(self, value, attr, obj, **kwargs):
        if value is None:
            return []
        return value

    def _deserialize(self, value, attr, data, **kwargs):

        if not isinstance(value, list):
            return []

        value = list(filter(None, value))
        return value


class RetrieveSchema(Schema):
    class Meta:

        unknown = INCLUDE
    cpf_cnpj = ClearRegister()
    name = fields.String(required=True)
    provinces = ClearProvince()
    cities = ClearList()
    target_id = fields.Integer(required=True)
    service_id = fields.Integer(required=True)
    webhook = fields.String(required=True)
