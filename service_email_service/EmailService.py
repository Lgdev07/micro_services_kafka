import sys
sys.path.append(sys.path[0] + "/..")

from common_kafka.KafkaConsumer import KafkaConsumer

consumer = KafkaConsumer('EmailService', ['ECOMMERCE_SEND_EMAIL'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    print('Received message: {}'.format(msg.value().decode('utf-8')))

consumer.close()