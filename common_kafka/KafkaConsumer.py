from confluent_kafka import Consumer

class KafkaConsumer(Consumer):
  def __init__(self, group_id, topics):
    self.group_id = group_id
    self.topics = topics

    configuration = {
      'bootstrap.servers': 'localhost:9092',
      'group.id': self.group_id,
      'auto.offset.reset': 'earliest'
    }

    super().__init__(configuration)

    return self.subscribe(self.topics)


