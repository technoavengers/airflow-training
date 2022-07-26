from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2022, 3, 1, 1),
    'owner': 'Airflow'
}

with DAG(dag_id='catchup_false', schedule_interval="0 * * * *", default_args=default_args, tags=['basic_dags'],catchup=False) as dag:
    
    task_1 = DummyOperator(task_id='dummy_task_1')
    
    task_2 = DummyOperator(task_id='dummy_task_2')
    
    task_1 >> task_2