import boto3
s3_resource = boto3.client("s3")

objects = s3_resource.list_objects(Bucket="akawasaiboto3tutorial1")["Contents"]



# if len(objects) > 0:
#     print("Objects exists")

for object in objects:
    print(object["Size"])

# just adding a comment to test out github