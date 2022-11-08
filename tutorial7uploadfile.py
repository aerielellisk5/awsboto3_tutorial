import boto3
import os
import glob

s3_resource = boto3.client("s3")

s3_resource.upload_file(
    Filename="aviandtj.jpg",
    # does the file need to be in the same folder? YES
    Bucket="akawasaiboto3tutorial1",
    Key="uploadtest.png"
)


cwd=os.getcwd()
cwd=cwd+"/AWSBOTO3_TUTORIAL/"

files = glob.glob(cwd+"*.jpg")
# this will grab all the files with .png

print(files)

for file in files:
    s3_resource = boto3.client("s3")
    s3_resource.upload_file(
    Filename=file,
    Bucket="akawasaiboto3tutorial1",
    Key=file.split("/")[-1]
    # split by the "/" and get the last part of the $PATH that will give the actual name of the file at the end
)