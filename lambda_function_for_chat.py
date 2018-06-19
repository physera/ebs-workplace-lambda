from botocore.vendored import requests
import os
import json


def parse_message(message):
    foo = [x.split(": ") for x in filter(None, message.split("\n"))]
    if len(foo) > 0:
        return dict(foo)
    else:
        return {}

def lambda_handler(event, context):
    headers = {"Authorization": "Bearer {}".format(os.environ['FB_API_TOKEN']),
               "content-type": "application/json"}
    url = "https://graph.facebook.com/me/messages"
    
    message = event['Records'][0]['Sns']['Message']
    fields = parse_message(message)
    
    if 'Application' in fields and 'Environment' in fields and 'Environment URL' in fields and 'Message' in fields:
        app = fields.get("Application", "App")
        post = "{} ({}): {}".format(app, fields["Environment"], fields["Message"])
    else:
        post = message
        
    data = {
        'recipient': {'thread_key': os.environ['FB_THREAD_ID']},
        'message': {'text': post}
    }
    requests.post(url, headers=headers, data=json.dumps(data)).json()
    