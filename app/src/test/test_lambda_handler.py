from app.src.lambda_handler import call_lambda
import unittest
import boto3
from moto import mock_sqs, mock_s3


class test_lambda_handler(unittest.TestCase):

    def setup(self):
        client = boto3.client("sqs")
        queue_test = client.create_queue(QueueName='test-queue')
        s3 = boto3.client('s3')
        s3.create_bucket(Bucket='test-bucket')
        file = open('upload_test_file.txt', 'r')
        s3.put_object(
            Body=file.read(),
            Bucket='test-bucket',
            Key='test-file',
        )

    @mock_sqs
    @mock_s3
    def test_sucess_send_message(self):
        self.setup()
        queue_url = 'https://sqs.us-east-1.amazonaws.com/123456789012/test-queue'
        event = {'queue_url': queue_url, 'message': 'Hello World', 'bucket': 'test-bucket', 'key': 'test-file'}
        res = call_lambda(event, None)

        self.assertTrue(res["queue"])
        self.assertTrue('9' in res['bucket'])


if __name__ == '__main__':
    unittest.TestCase()
