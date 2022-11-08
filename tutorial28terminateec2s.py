import boto3
import json

# this code will print a lot prettier!
# print(json.dumps(response, indent=2, default=str))

ec2_resource = boto3.resource("ec2")