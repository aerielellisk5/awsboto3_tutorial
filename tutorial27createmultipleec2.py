import boto3
import json

# this code will print a lot prettier!
# print(json.dumps(response, indent=2, default=str))

ec2_resource = boto3.resource("ec2")

new_resource = ec2_resource.create_instances(
    ImageId='ami-09d3b3274b6c5d4aa',
    InstanceType='t2.micro',
    MaxCount=3,
    MinCount=3,
)

print(len(new_resource))