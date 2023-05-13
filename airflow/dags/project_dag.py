from airflow import DAG
from airflow.decorators import task
from airflow.operators.python import PythonOperator
from airflow.exceptions import AirflowException
from airflow.providers.postgres.hooks.postgres import PostgresHook

from datetime import datetime
import pandas as pd


def select_query(**kwargs):
    ti = kwargs['ti']
    pg_hook = PostgresHook(postgres_conn_id='posscon')
    conn = pg_hook.get_conn()
    print('postgres connect success')
    cursor = conn.cursor()
    df = pd.read_sql('select * from public.stg;', conn)
<<<<<<< HEAD
    cursor.execute('truncate only public.stg;')
    conn.commit()
    conn.close()
=======
    cursor.execute('delete from public.stg;')
    conn.commit()
    conn.close()
    print(df)
>>>>>>> 97b8359fff2ffadab12e64a60cb30cd0fd5fd56b
    df = df.astype({'temperature': 'int32'})
    df_to_load = df[df['temperature'] >= 0]
    json_df = df_to_load.to_json()
    ti.xcom_push(value=json_df, key='out_df')

def insert_into_dds(json_df):
    df = pd.read_json(json_df)
<<<<<<< HEAD
=======
    print(df)
>>>>>>> 97b8359fff2ffadab12e64a60cb30cd0fd5fd56b
    pg_hook = PostgresHook(postgres_conn_id='posscon')
    conn = pg_hook.get_conn()
    print('postgres connect success')
    cursor = conn.cursor()
    for i in df.values:
        cursor.execute("""INSERT INTO public.dds(date, id, points, temperature, hash) VALUES (%s, %s, %s, %s, %s);""", [i[0], i[1], i[2], i[3], i[4]])
    print('Insert process success')
    conn.commit()
    conn.close()

with DAG (
    dag_id='bigdata_project_dag',
    start_date=datetime(2023, 5, 3),
    catchup=False,
    schedule_interval="* * * * *"
) as dag:
    py_select_stg = PythonOperator(task_id='select_step', python_callable=select_query)

    py_insert_dds = PythonOperator(task_id='insert_step', python_callable=insert_into_dds, op_args=['{{ti.xcom_pull(key="out_df")}}'])

    py_select_stg >> py_insert_dds

    