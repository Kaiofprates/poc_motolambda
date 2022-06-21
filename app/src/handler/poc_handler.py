from app.src.handler.Handler import Handler


class POCHandler(Handler):
    def handle(self, event, context):
        queue_url = event['queue_url']
        message = event['message']
        bucket = event['bucket']
        key = event['key']
        result_bucket = self.bucket.get_file(bucket, key)
        result_queue = self.queue.send_message(queue_url, message)

        return {"queue": result_queue, "bucket": result_bucket}
