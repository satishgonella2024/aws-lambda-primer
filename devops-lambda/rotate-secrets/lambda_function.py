import boto3
import secrets
import string

secrets_manager = boto3.client("secretsmanager")

def lambda_handler(event, context):
    secret_name = "MyDatabasePassword"
    new_password = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(16))
    
    secrets_manager.put_secret_value(SecretId=secret_name, SecretString=new_password)
    
    return {"statusCode": 200, "body": "Password rotated successfully"}