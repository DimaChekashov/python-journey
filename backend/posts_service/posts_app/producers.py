from confluent_kafka import Producer
import json
from django.conf import settings

class PostProducer:
    def __init__(self):
        self.producer = Producer({
            'bootstrap.servers': settings.KAFKA_BROKER_URL
        })

    def send_post_created(self, post_data):
        self.producer.produce(
            'posts.created',
            json.dumps(post_data).encode('utf-8'))
        self.producer.flush()