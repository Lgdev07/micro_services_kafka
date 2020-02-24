from confluent_kafka import Producer

class KafkaProducer():
  def __init__(self):
    self.messages = []
    self.producer = Producer({'bootstrap.servers': 'localhost:9092'})
  
  def __repr__(self):
    return self.messages

  def new_message(self, topic, value, key=None):
    self.messages.append({
      "topic": topic,
      "value": value,
      "key": key,
    })

    return self

  def push(self):
    self.producer.poll(0)
    for message in self.messages:
      self.producer.produce(
        message['topic'], 
        message['value'],
        message['key'], 
        callback=self.delivery_report
      )
      self.producer.flush()

  def delivery_report(self, err, msg):
      if err is not None:
          print('Message delivery failed: {}'.format(err))
      else:
          print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


