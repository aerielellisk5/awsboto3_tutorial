import boto3
import json

# this code will print a lot prettier!
# print(json.dumps(response, indent=2, default=str))

# ec2_client = boto3.client("ec2")

# x = ec2_client.describe_instances()

# print(x.keys())
# dict_keys(['Reservations', 'ResponseMetadata'])

# print(json.dumps(x["Reservations"], indent=2, default=str))

# data = (x['Reservations'])
# li = []

# for instances in data:
#     instance  = instances["Instances"]
#     for ids in instance:
#         instance_id = ids["InstanceId"]
#         li.append(instance_id)

# probably need to check if the one that cnat be deleted has a specific value, if it does, it wont get added to the list

ec2_client = boto3.client("ec2")
x = ec2_client.describe_instances()
data = (x['Reservations'])
li = []

for instances in data:
    variables = instances["Instances"]
    # print(json.dumps(variables, indent=2, default=str))
    for variable in variables:
        if (variable['State']['Name']) == 'running':
            instance_id = variable["InstanceId"]
            li.append(instance_id)
    
ec2_client.terminate_instances(InstanceIds=li)



# ec2_client.terminate_instances(
#     InstanceIds=li
#     )

