# -*- coding: utf-8 -*-
import json
import os
import logging

from aliyunsdkcore import client
from aliyunsdkcore.auth.credentials import StsTokenCredential
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkfnf.request.v20190315 import ReportTaskSucceededRequest

def handler(event, context):
  logger = logging.getLogger()
  evt = json.loads(event)
  logger.info("Handling event: %s", evt)

  creds = context.credentials
  sts_token_credential = StsTokenCredential(creds.access_key_id, creds.access_key_secret, creds.security_token)
  fnf_client = client.AcsClient(region_id=context.region, credential=sts_token_credential)

  request = ReportTaskSucceededRequest.ReportTaskSucceededRequest()
  request.set_TaskToken(evt["taskToken"])
  request.set_Output(json.dumps(evt["output"]))

  return fnf_client.do_action_with_exception(request)
