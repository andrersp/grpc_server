from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from os import environ as env

engine = create_engine(env.get("DATABASE_URL"), echo=False)
Base = declarative_base()
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)


def create_db():
    Base.metadata.create_all(engine)
