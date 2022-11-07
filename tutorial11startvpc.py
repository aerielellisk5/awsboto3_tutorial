import boto3
client = boto3.client("ec2")

# print(client.create_vpc??)
# need to find something similar I can use here to see what else I can use it

print(client.create_vpc(CidrBlock="10.0.0.0/16"))

