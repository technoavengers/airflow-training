from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta
import time

default_args = {
    'start_date': datetime(2022, 1, 1),
    'owner': 'Airflow'
}

def first_task():
    print('This is first task')

def second_task():
    print('This is second task')
    time.sleep(5)

def third_task():
    print('This is third task')

with DAG(dag_id='wait_for_downstream', schedule_interval= "0 0 * * *", default_args=default_args,tags=['basic_dags']) as dag:
    
    task_1 = PythonOperator(task_id='task_1', python_callable=first_task, wait_for_downstream=True)
    
    task_2 = PythonOperator(task_id='task_2', python_callable=second_task)

    task_3 = PythonOperator(task_id='task_3', python_callable=third_task)

    task_1 >> task_2 >> task_3