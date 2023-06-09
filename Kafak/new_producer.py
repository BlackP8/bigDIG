import time 
import json 
import random 
from datetime import datetime, timedelta
from kafka import KafkaProducer
import pandas as pd
from conf import kafka_conn, kafka_topic
from time import sleep


def main():
    utc_code = [2, 3, 3, 5, 5, 7, 8, 9, 10, 11]
    date_list = date_scan(utc_code)
    # id_list = id_gen(last_id)
    id_list = ['8820ddfs', '8821ddfs', '8822ddfs', '8823ddfs', '8824ddfs', '8825ddfs', '8826ddfs', '8827ddfs', '8828ddfs', '8829ddfs']
    # Калининград, Смоленск, Москва, Илек, Ханты-Мансийск, Лесосибирск, Иркутск, Чита, Артем, Томари
    points_list = ['54.710162, 20.510137', '54.782621, 32.045275', '55.755865, 37.617520', '51.531921, 53.375013', '61.003109, 69.018735', 
                   '58.221749, 92.503414', '52.289585, 104.280087', '52.033676, 113.500301', '43.353031, 132.180344', '47.761061, 142.063513']
    temp_list = temp_gen()
    id_hash_list = hash_func(id_list)

    df = pd.DataFrame({"date": date_list, "id": id_list, "points": points_list, "temperature": temp_list, "hash": id_hash_list})
    return df


# date_scaner
def date_scan(hours):
    ans = []
    for i in hours:
        current_date = datetime.now() - timedelta(hours = (3 - i))
        ans.append(current_date)
    return ans


# temp generation
def temp_gen():
    temp = []
    for i in range(10):
        temp.append(random.randint(-20, 20))
    return temp


# hash func
def hash_func(arr):
    ans = []
    for i in arr:
        hashed_i = hash(i)
        ans.append(hashed_i)
    return ans


# id gen
def id_gen(last_id):
    list_id = []
    list_id = []
    for _ in range(10):
        last_id = str(int(last_id[:4]) + 1) + last_id[4:]
        list_id.append(last_id)
    return list_id



# Messages will be serialized as JSON 
def serializer(message):
    return json.dumps(message).encode('utf-8')

producer = KafkaProducer(
    bootstrap_servers=[kafka_conn],
    value_serializer=serializer
)

# last_id = '1120ddfs'

while True:
    df = main()

    for index, row in df.iterrows():
        print(f'Producing message @ {datetime.now()} | Message = {str(row)}')
        producer.send(kafka_topic, row.to_json())
        # last_id = row[1]
        
    sleep(1)