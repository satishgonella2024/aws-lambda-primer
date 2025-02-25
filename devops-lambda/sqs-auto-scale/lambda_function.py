import boto3

autoscaling = boto3.client("autoscaling")

def lambda_handler(event, context):
    queue_size = int(event["Records"][0]["messageAttributes"]["QueueSize"]["stringValue"])
    
    if queue_size > 100:
        autoscaling.set_desired_capacity(AutoScalingGroupName="MyASG", DesiredCapacity=5)
    elif queue_size < 10:
        autoscaling.set_desired_capacity(AutoScalingGroupName="MyASG", DesiredCapacity=1)
    
    return {"statusCode": 200, "body": "Auto Scaling adjusted"}