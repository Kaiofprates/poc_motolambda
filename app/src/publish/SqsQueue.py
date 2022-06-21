from app.src.publish.Queue import Queue
import boto3


class SqsQueue(Queue):
    def __init__(self):
        self.client = boto3.client('sqs', region_name='us-east-1')

    def send_message(self, queue_url, message_body):

        response = self.client.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )

        if response['ResponseMetadata']['HTTPStatusCode'] == 200:
            return True
        else:
            return False
