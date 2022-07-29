from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
import airflow

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2022, 7, 26, 8,55),
    'owner': 'Airflow'
}

with DAG(dag_id='start_after_current', schedule_interval='*/5 * * * *', default_args=default_args, tags=['basic_dags']) as dag:
    
    task_1 = DummyOperator(task_id='dummy_task_1')
    
    task_2 = DummyOperator(task_id='dummy_task_2')

    task_3 = DummyOperator(task_id='dummy_task_3')

    task_4 = DummyOperator(task_id='dummy_task_4')
    
    task_1 >> [task_2,task_3] >> task_4