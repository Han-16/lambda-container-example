import boto3
import os
import json
import io
import csv
import numpy as np
import pandas as pd

ACCESS_KEY = os.environ.get("ACCESS_KEY")
SECRET_KEY = os.environ.get("SECRET_KEY")
BUCKET = "clerker-ai.bucket"

s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
    )

def download_file_from_s3(file_name, key):
    s3_client.download_file(BUCKET, key, file_name)

def unzip_file(file_name):
    os.system(f"unzip /tmp/{file_name} -d /tmp/example.csv")


def handler(event, context):
    file_name = event["mp3FileUrl"]
    key = event["mp3FileUrl"]
    download_file_from_s3(file_name, key)
    print(os.listdir("/tmp"))
    unzip_file(file_name)
    data = pd.read_csv(f"tmp/example.csv")
    
    return {
        "statusCode": 200,
        "body": json.dumps(data.head())
    }