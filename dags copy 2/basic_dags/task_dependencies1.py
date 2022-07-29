from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2022, 3, 1, 1),
    'owner': 'Airflow'
}

with DAG(dag_id='task_dependencies_within_dag', schedule_interval=None, default_args=default_args, tags=['basic_dags'],catchup=False) as dag:
    
    task_1 = DummyOperator(task_id='task1')
    
    task_2 = DummyOperator(task_id='task2')

    task_3 = DummyOperator(task_id='task3')

    task_4 = DummyOperator(task_id='task4')

    task_5 = DummyOperator(task_id='task5')
    
    task_1 >> task_2 >> [task_3,task_4] >> task_5