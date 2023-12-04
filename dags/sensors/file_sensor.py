import airflow
from pendulum import datetime
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.S3_hook import S3Hook
from airflow.decorators import task
from airflow.operators.email_operator import EmailOperator
from airflow.contrib.sensors.file_sensor import FileSensor
from airflow.operators.python import PythonOperator

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1)
}

def process_file():
    file1 = open("/tmp/transactions.csv", "r+")
    print(file1.read())
    print("file has been processed")


with DAG(dag_id='file_sensor', schedule_interval='@daily',default_args=default_args,tags=['sensors']) as dag:
     t1 = FileSensor(
        task_id='check_file_exists',
        filepath='/tmp/transactions.csv',
        poke_interval=10,
        timeout=150,
        soft_fail=True
    )
     
     t2 = PythonOperator(
            task_id="task1",
            python_callable=process_file)
     
     t1 >> t2 
