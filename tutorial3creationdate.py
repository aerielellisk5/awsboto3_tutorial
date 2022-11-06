import boto3
s3_resource = boto3.client("s3")

# print(s3_resource)
# print(s3_resource.list_buckets()["Buckets"][0]["Name"])
# create_date = s3_resource.list_buckets()["Buckets"][0]["CreationDate"]

# print(create_date.strftime("%d%m%y_%H:%M"))

create_date = s3_resource.list_buckets()["Buckets"]
for bucket in create_date:
    print((bucket["Name"]))
    print((bucket["CreationDate"]))