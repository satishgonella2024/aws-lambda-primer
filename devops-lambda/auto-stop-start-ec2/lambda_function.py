import boto3
import os

ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    action = os.getenv("ACTION", "stop")  # Set "start" or "stop" via environment variable
    
    instances = ["i-xxxxxxxxxxxxxxxxx", "i-yyyyyyyyyyyyyyyyy"]  # Replace with your EC2 instance IDs

    if action == "stop":
        ec2.stop_instances(InstanceIds=instances)
        return {"statusCode": 200, "body": "Stopped instances: " + str(instances)}
    else:
        ec2.start_instances(InstanceIds=instances)
        return {"statusCode": 200, "body": "Started instances: " + str(instances)}