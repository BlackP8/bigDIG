import json 
from kafka import KafkaConsumer
import pandas as pd
import psycopg2 as ps2
from conf import host, password, port, user, db, kafka_topic, kafka_conn


connection = ps2.connect(host=host, port=port, database=db, user=user, password=password)
cursor = connection.cursor()

consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_conn
)
for message in consumer:
    str_output = json.loads(json.loads(message.value))
    df = pd.DataFrame(str_output, index=[0])
    for i in df.values:
        cursor.execute("""INSERT INTO public.stg(date, id, points, temperature, hash) VALUES (%s, %s, %s, %s, %s);""", [i[0], i[1], i[2], i[3], i[4]])
        connection.commit()
        print('Successful insert')

connection.close()