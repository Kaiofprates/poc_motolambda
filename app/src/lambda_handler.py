from app.src.handler.poc_handler import POCHandler
from app.src.publish.SqsQueue import SqsQueue
from app.src.bucket.BucketS3 import BucketS3


def call_lambda(event, context):
    handler = POCHandler(SqsQueue(), BucketS3())
    return handler.handle(event, context)


if __name__ == '__main__':
    call_lambda({'queue_url': 'https://sqs.us-east-1.amazonaws.com/123456789012/test-queue',
                 'message': 'Hello World', 'bucket': 'test-bucket', 'key': 'test-file'},
                None)
