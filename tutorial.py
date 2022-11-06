import boto3
aws_resource=boto3.resource('s3')
bucket=aws_resource.Bucket("akawasaiboto3tutorial1")
# remember that the bucketname needs to be unique!

response = bucket.create(
    ACL='private'
)

print(response)

