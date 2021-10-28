# -*- coding: utf-8 -*-

from requests import post
import json

from grpc_server.core.exceptions import FatalError


class Responder(object):

    def sucess(self, service_id: int, target_id: int, webhook_url: str, result: list, success: bool = True):

        content = {
            "service": service_id,
            "block_content": result,
            "target_id": target_id,
            "sucess": success
        }
        result = post(webhook_url, json=content)
