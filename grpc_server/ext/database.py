from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy.exc import OperationalError, StatementError
from sqlalchemy.pool import NullPool
from time import sleep
import logging


class RetryingQuery(BaseQuery):
    __retry_count__ = 3

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __iter__(self):
        attempts = 0
        while True:
            attempts += 1
            try:
                return super().__iter__()
            except OperationalError as ex:
                if "could not translate host name" in str(ex):
                    raise
                if attempts < self.__retry_count__:
                    logging.error(
                        "Database connection error: {} - sleeping for {}s"
                        " and will retryyes (attempt #{} of {})".format(
                            ex, 5, attempts, self.__retry_count__
                        )
                    )
                    sleep(5)
                    continue
                else:
                    raise
            except StatementError as ex:
                self.session.rollback()


db = SQLAlchemy(query_class=RetryingQuery,
                engine_options={"poolclass": NullPool})


def init_app(app):
    db.init_app(app)
