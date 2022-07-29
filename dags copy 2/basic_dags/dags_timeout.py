from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta
import time

default_args = {
    'start_date': datetime(2022, 7, 24, 6),
    'owner': 'Airflow'
}

def first_task():
    print('This is first task')

def second_task():
    print('This is second task')
    #time.sleep(20)

def third_task():
    print('This is third task')

with DAG(dag_id='dags_timeout', schedule_interval= "0 * * * *", default_args=default_args,tags=['basic_dags'],dagrun_timeout=timedelta(seconds=10)) as dag:
    
    task_1 = PythonOperator(task_id='task_1', python_callable=first_task)
    
    task_2 = PythonOperator(task_id='task_2', python_callable=second_task)

    task_3 = PythonOperator(task_id='task_3', python_callable=third_task)

    task_1 >> task_2 >> task_3