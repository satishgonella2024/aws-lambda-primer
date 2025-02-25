import json
import requests
import os

SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def lambda_handler(event, context):
    log_data = json.loads(event["Records"][0]["Sns"]["Message"])
    error_message = log_data.get("logEvents", [{}])[0].get("message", "")

    if "ERROR" in error_message:
        slack_message = {"text": f"🚨 AWS CloudWatch Alert: {error_message}"}
        requests.post(SLACK_WEBHOOK_URL, json=slack_message)
    
    return {"statusCode": 200, "body": "Logs checked and alerts sent"}