import boto3
s3_resource = boto3.client("s3")
# bucketname = akawasaiboto3tutorial1


s3_resource.delete_object(Bucket='akawasaiboto3tutorial1', Key='halloween.png')
# this will delete a single object


import os
import glob

objects = (s3_resource.list_objects(Bucket='akawasaiboto3tutorial1'))["Contents"]

# print(len(objects))

# this will find all the objects and then delete from the bucket by iterating over the object
for object in objects:
    response = s3_resource.delete_object(Bucket='akawasaiboto3tutorial1', Key = object["Key"])
    print(response)


