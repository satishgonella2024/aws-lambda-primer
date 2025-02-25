import json
import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']
    
    print(f"New file {file_name} uploaded to bucket {bucket_name}")
    
    return {
        "statusCode": 200,
        "body": json.dumps(f"File {file_name} uploaded!")
    }