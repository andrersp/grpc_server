import sentry_sdk
from os import environ as env
from sentry_sdk.integrations.celery import CeleryIntegration


def init_celery(app, celery):
    """Add flask app context to celery.Task"""

    task_base = celery.Task

    class ContextTask(task_base):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return task_base.__call__(self, *args, **kwargs)

    sentry_sdk.init(
        dsn=env.get('SENTRY_DSN'),
        integrations=[CeleryIntegration()]
    )

    celery.Task = ContextTask