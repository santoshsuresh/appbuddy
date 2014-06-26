from __future__ import absolute_import
from annoying.functions import get_object_or_None
from celery import shared_task
from io import BytesIO
from rest_framework.parsers import JSONParser
from .models import *


@shared_task
def log_appbuddy_install(*args, **kwargs):
    log_data = kwargs['log_data']
    stream = BytesIO(log_data)
    data = JSONParser().parse(stream)
    user = get_object_or_None(AppBuddyUser, device_id=data.get('device_id'))
    if user is None:
        agent_info = None
        agent = get_object_or_None(AgentInfo, agent_id=data.get('agent_id'))
        if len(agent) > 0:
            agent_info = agent[0]

        print agent
    pass