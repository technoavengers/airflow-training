from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
import airflow
from airflow.operators.bash import BashOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2022, 7, 27, 6, 25),
    'owner': 'Airflow'
}

with DAG(dag_id='specific_queues', schedule_interval="0/5 * * * *", default_args=default_args, tags=['queues']) as dag:
    
    task_1 = BashOperator(
            task_id='cpu_intensive_task',
            bash_command='sleep 60',
            queue='worker_cpu'
            ) 
    
    task_2 = BashOperator(
            task_id='simple_task',
            bash_command='sleep 60',
            ) 

    task_3 = BashOperator(
            task_id='spark_task',
            bash_command='sleep 60',
            queue='worker_cpu'
            ) 

    task_4 = DummyOperator(task_id='dummy_task_4')
    
    [task_1,task_2,task_3] >> task_4
    
    




  