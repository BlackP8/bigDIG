import json
import psycopg2
import pandas as pd

with open('out.json') as f:
    data = json.load(f)

conn = psycopg2.connect(host="localhost", database="greenplumdb", user="admin", password="qwerty", port='5432')
cur = conn.cursor()

date_list = pd.json_normalize(data['date']).values.flatten().tolist()
id_list = pd.json_normalize(data['id']).values.flatten().tolist()
points_list = pd.json_normalize(data['points']).values.flatten().tolist()
temp_list = pd.json_normalize(data['temperature']).values.flatten().tolist()
hash_list = pd.json_normalize(data['hash']).values.flatten().tolist()

for i in range(len(date_list)):
    cur.execute("INSERT INTO stg(date, id, points, temperature, hash) VALUES (%s, %s, %s, %s, %s)",
                (date_list[i], id_list[i], points_list[i], temp_list[i], hash_list[i]))

conn.commit()
cur.close()
conn.close()
