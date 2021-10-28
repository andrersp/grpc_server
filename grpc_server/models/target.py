# -*- coding: utf-8 -*-
from grpc_server.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class ModelTarget(db.Model, SerializerMixin):

    serialize_rules = (
        "-id"
    )

    __tablename__ = "target"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    cpf_cnpj = db.Column(db.String(20))
    last_update = db.Column(db.DateTime, default=db.func.now())

    def __repr__(self):
        return "<target %r>" % self.cpf_cnpj

    # Save Target Into DB
    def save_target(self):
        db.session.add(self)
        db.session.commit()

    def update_target(self):
        self.last_update = db.func.now()
        self.save_target()
