import boto3
import json
client = boto3.client("ec2")


#How to describe all vpc that are available in your account
response = client.describe_vpcs()

# this code will print a lot prettier!
# print(json.dumps(response, indent=2, default=str))

no_of_vps = response["Vpcs"]

# print(len(no_of_vps))

# for vpc in no_of_vps:
#     print(vpc["VpcId"])


x = client.describe_vpcs(VpcIds=["vpc-028bdff8f68e23608"])
print(json.dumps(x, indent=2,default=str))