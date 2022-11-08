import boto3
import json

# this code will print a lot prettier!
# print(json.dumps(response, indent=2, default=str))


ec2_client = boto3.client("ec2")
x = ec2_client.describe_instances()
# print(json.dumps(x, indent=2, default=str))

# print(json.dumps(x["Reservations"], indent=2, default=str))

# print(x["Reservations"])

data = x["Reservations"]
# print(len(data))

# print(json.dumps(data, indent=2, default=str))

# data_instance = data["Instances"]
# print(len(data_instance))

for i in range(len(data)):
    print(data[i]["Instances"][0]["InstanceId"])




















# print(len(x["Reservations"]))

# data = x["Reservations"][0]
# # print(json.dumps(data, indent=2, default=str))


# # print(data["Instances"])
# print(json.dumps(data["Instances"], indent=2, default=str))

# # print(len(data_instance))
