import boto3
resource=boto3.resource('s3')

bucket_list = (list(resource.buckets.all()))
# used to be all_buckets
print(len(bucket_list))
# for bucket in all_buckets:
#     print(bucket.name)



