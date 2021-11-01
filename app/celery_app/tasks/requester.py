# -*- coding: utf-8 -*-
from sentry_sdk import capture_exception
import arrow
from datetime import datetime

from app.app import celery
from app.ext.responder import Responder
from app.core.exceptions import CustomError, FatalError
from celery.exceptions import MaxRetriesExceededError


@celery.task(bind=True, default_retry_delay=1 * 60, max_retries=10)
def request(self, data):
    # data is a dict
    # -- happy code! --

    name = data.get("name")
    cpf_cnpj = data.get("cpf_cnpj")
    service_id = data.get("service_id")
    target_id = data.get("target_id")

    webhook_url = data.get("webhook")
    update = data.get("update")

    result = {}

    try:
        Responder().sucess(service_id, target_id, webhook_url, result)
    except FatalError as exc:
        capture_exception(exc)
        Responder().sucess(service_id, target_id, webhook_url, result, False)
        return False

    except Exception as exc:
        logging.info(exc)
        try:
            self.retry()
        except MaxRetriesExceededError as e:
            capture_exception(exc)
            return False
    else:
        return {"sucess": True, "report": name}
