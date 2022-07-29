from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
import airflow

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2022, 7, 27, 6, 25),
    'owner': 'Airflow'
}

with DAG(dag_id='first_basic_dag_1', schedule_interval="0/5 * * * *", default_args=default_args, tags=['basic_dags']) as dag:
    
    task_1 = DummyOperator(task_id='dummy_task_1')
    
    task_2 = DummyOperator(task_id='dummy_task_2')

    task_3 = DummyOperator(task_id='dummy_task_3')

    task_4 = DummyOperator(task_id='dummy_task_4')

    task_5 = DummyOperator(task_id='dummy_task_5')

    task_6 = DummyOperator(task_id='dummy_task_6')

    task_7 = DummyOperator(task_id='dummy_task_7')
    
    task_1 >> [task_2,task_3] >> task_4

    task_1 >> task_5

    task_6 >> task_7
    
    




  