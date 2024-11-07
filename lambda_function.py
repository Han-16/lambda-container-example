import boto3
import os
import json
import io
import csv

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
        s3_client.download_file(BUCKET_NAME, object_name, '/tmp/example.csv')
    except Exception as e:
        print(e)
        raise e
    

def handler(event, context):
    object_name = event["mp3FileUrl"]
    download_file_from_s3(object_name)
    print(os.listdir("/tmp"))
    