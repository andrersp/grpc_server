# -*- coding: utf-8 -*-
from sqlalchemy.dialects.postgresql import JSON, ARRAY

from app.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class MoviesDb(db.Model, SerializerMixin):

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    adult = db.Column(db.Boolean)
    genres = db.Column(ARRAY(JSON))
