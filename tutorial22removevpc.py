# this code will print a lot prettier!
# print(json.dumps(response, indent=2, default=str))

import boto3
import json

client = boto3.client("ec2")

response = client.delete_vpc(
    VpcId='vpc-0f127b78e4f712e9e'
)

print(json.dumps(response, indent=2, default=str))