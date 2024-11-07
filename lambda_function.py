import boto3
import os
import json
import io
import zipfile

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")
BUCKET_NAME = "clerker-ai.bucket"

s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )

def download_file_from_s3(object_name):
    try:
        s3_client.download_file(BUCKET_NAME, object_name, '/tmp/example.zip')
    except Exception as e:
        print(e)
        raise e
    

def handler(event, context):
    object_name = event["mp3FileUrl"]
    download_file_from_s3(object_name)
    print("Downloaded file from S3")
    print(os.listdir("/tmp"))
    print("unzip the file")
    with zipfile.ZipFile('/tmp/example.zip', 'r') as zip_ref:
        zip_ref.extractall('/tmp')
    print("Unzipped the file")
    print(os.listdir("/tmp"))    