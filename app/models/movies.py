# -*- coding: utf-8 -*-
from sqlalchemy.dialects.postgresql import JSON, ARRAY

from sqlalchemy import Column, Integer, String, Boolean
from ext.database import Base, Session


class MoviesDb(Base):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String())
    adult = Column(Boolean)
    language = Column(String(10))
    genres = Column(ARRAY(JSON))

    def save_movie(self):
        session = Session()
        session.add(self)
        session.commit()
