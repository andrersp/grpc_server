# -*- coding: utf-8 -*-
"""
Configure Celery. See the configuration guide at ->
http://docs.celeryproject.org/en/master/userguide/configuration.html#configuration
"""

# Broker settings.
import os

broker_url = os.environ.get('RABBITMQ_URL')
broker_heartbeat = 0

# List of modules to import when the Celery worker starts.
# i.e.: 'app.celery_app.tasks.service_x'
imports = (

)

# Using the database to store task state and results.

result_backend = os.environ.get("REDIS_URL")
result_persistent = True


accept_content = ['json', 'application/text']

result_serializer = 'json'
timezone = "UTC"
