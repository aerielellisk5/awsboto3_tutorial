import boto3
import json

ec2_resource = boto3.cleint("ec2")

ec2_resource.create_instances(ImageId='GOESHERE', 
    InstanceType = 't2.micro',
    MaxCount = 1,
    MinCount = 1
)