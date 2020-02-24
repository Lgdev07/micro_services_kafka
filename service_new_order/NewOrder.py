import json
import sys
sys.path.append(sys.path[0] + "/..")

from common_kafka.KafkaProducer import KafkaProducer
from Order import Order

# Received a new order from client, we send it to our message broker
order1 = Order('Iphone11', '1652,10', 'luan.gomes@hotmail.com')
order1_json = json.dumps(order1.__dict__)

producer = KafkaProducer()

producer.new_message('ECOMMERCE_NEW_ORDER', order1_json)
producer.new_message('ECOMMERCE_SEND_EMAIL', order1.email)

producer.push()
