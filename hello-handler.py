import os
import json

def hello(event, context):
    if 'queryStringParameters' in event.keys():
        body = {
            "name": event.get('queryStringParameters').get('name'),
            "msg": "hello",
            "env": os.environ['KEY1'] 
        }
    else:
        body = {
            "name": "none",
            "msg": "please name parameter"
        }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response