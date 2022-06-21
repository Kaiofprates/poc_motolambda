class Handler(object):
    def __init__(self, queue, bucket):
        self.queue = queue
        self.bucket = bucket

    def handle(self, event, context):
        raise Exception("Not implemented")
