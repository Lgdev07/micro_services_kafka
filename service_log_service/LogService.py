import sys
sys.path.append(sys.path[0] + "/..")

from datetime import datetime
from common_kafka.KafkaConsumer import KafkaConsumer

consumer = KafkaConsumer('LogService', ['^ECOMMERCE.*'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('+=' * 10)
    print(f'Received message FROM: {msg.topic()}')
    print(f'Value: {msg.value()}')
    print(f'Time: {datetime.now()}')

consumer.close()