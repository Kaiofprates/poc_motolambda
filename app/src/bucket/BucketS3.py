import boto3
from app.src.bucket.S3 import S3


class BucketS3(S3):
    def __init__(self):
        self.client = boto3.client('s3', region_name='us-east-1')

    def get_file(self, bucket, key):
        response = self.client.get_object(
            Bucket=bucket,
            Key=key
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return response['Body'].read().decode('utf-8')
        else:
            return False