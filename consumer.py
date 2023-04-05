from confluent_kafka import Consumer
import pandas as pd


c = Consumer({'bootstrap.servers': 'localhost:9092',
              'group.id': 'descount_product_group',
              'auto.offset.reset': 'earliest'})
c.subscribe(['product_topic'])

while True:
    msg = c.poll(1.0)
    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".fromat(msg.error()))
        continue
    print('Received message: {}'.format(msg.value().decode('utf-8')))


c.close()