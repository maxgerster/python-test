import os
import json
import pull.request
import pull.insert

URL = os.getenv('URL')
ENV_VAR_2 = os.getenv('ENV_VAR_2')
ENV_VAR_3 = os.getenv('ENV_VAR_3')

print("Loading function...")

def lambda_handler(event, context):
    try:
        print("Received event: " + json.dumps(event, indent=2))
        print(pull.request.request(event['URL']))
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda! Real Test')
        }
    except:
        print("An exception occured.")
