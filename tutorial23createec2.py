# import boto3
# import json

# client = boto3.client("ec2")

# print(ec2_resource.create_instances(ImageId='ami-09d3b3274b6c5d4aa', 
#     InstanceType = 't2.micro',
#     MaxCount = 1,
#     MinCount = 1
# )
# )

import boto3
# client = boto3.client("ec2")
# need to recreate my default vpc before I can do anything
# response = client.create_default_vpc()
# print(response)


ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-09d3b3274b6c5d4aa",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro"
    )

