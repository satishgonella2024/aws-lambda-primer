import boto3

ec2 = boto3.client("ec2")

def lambda_handler(event, context):
    security_groups = ec2.describe_security_groups()["SecurityGroups"]
    
    for sg in security_groups:
        for rule in sg.get("IpPermissions", []):
            for ip in rule.get("IpRanges", []):
                if ip["CidrIp"] == "0.0.0.0/0" and rule["FromPort"] == 22:
                    ec2.revoke_security_group_ingress(
                        GroupId=sg["GroupId"],
                        IpProtocol=rule["IpProtocol"],
                        FromPort=rule["FromPort"],
                        ToPort=rule["ToPort"],
                        CidrIp="0.0.0.0/0"
                    )
                    print(f"Removed public SSH access from {sg['GroupId']}")
    
    return {"statusCode": 200, "body": "Security groups fixed"}