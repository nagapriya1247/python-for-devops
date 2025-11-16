import boto3
from botocore.exceptions import ClientError

def list_buckets():
    s3 = boto3.client('s3')
    resp = s3.list_buckets()
    return [b['Name'] for b in resp.get('Buckets', [])]

def upload_file(bucket, key, filename):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(filename, bucket, key)
        return {"ok": True, "bucket": bucket, "key": key}
    except ClientError as e:
        return {"ok": False, "error": str(e)}

def download_file(bucket, key, filename):
    s3 = boto3.client('s3')
    try:
        s3.download_file(bucket, key, filename)
        return {"ok": True, "filename": filename}
    except ClientError as e:
        return {"ok": False, "error": str(e)}