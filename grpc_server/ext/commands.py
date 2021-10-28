from grpc_server.ext.database import db


def create_db():
    """Creates database"""
    db.create_all()


def init_app(app):
    with app.app_context():
        create_db()
