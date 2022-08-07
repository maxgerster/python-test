import json
import logging
import logging.config
import os

import pull.request
import pull.insert

# Environment vars
URL = os.getenv('URL')

# Logger configuration
logger = logging.getLogger(os.path.basename(__file__))
logging.basicConfig(level = logging.INFO, format = '%(asctime)s - %(levelname)-8s - %(name)s - %(message)s')

logger.info("Loading function...")

# Lambda function
def lambda_handler(event, context):
    try:
        logger.info("Received event: " + json.dumps(event, indent=2))
        # Request
        logger.info(pull.request.request(event['URL']))
        return {
            'statusCode': 200,
            'body': json.dumps('Hello from Lambda! Real Test')
        }
    except:
        logger.error("An exception occured.", exc_info=True)
