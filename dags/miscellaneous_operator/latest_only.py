from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
import airflow
from airflow.operators.latest_only import LatestOnlyOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2022, 7, 27),
    'owner': 'Airflow'
}


def is_wednesday(execution_date):
    return execution_date.weekday() == 2

with DAG(dag_id='latest_only', schedule_interval="@hourly", default_args=default_args, tags=['miscellaneous'],catchup=True) as dag:
    
    task_1 = DummyOperator(task_id='download_file')
    
    task_2 = DummyOperator(task_id='process_file')

    task_3 = DummyOperator(task_id='store_file')

    is_latest = LatestOnlyOperator(task_id="is_latest")

    task_4 = DummyOperator(task_id='notify')

    task_5 = DummyOperator(task_id='task_5')

    task_6 = DummyOperator(task_id='task_6')
    
    task_1 >> task_2 >> task_3  >> is_latest >> task_4 >> task_5
    
    task_3 >> task_6




  