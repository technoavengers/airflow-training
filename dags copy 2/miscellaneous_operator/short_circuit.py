from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
import airflow
from airflow.operators.python import ShortCircuitOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2022, 7, 27, 6, 25),
    'owner': 'Airflow'
}


def is_wednesday(execution_date):
    return execution_date.weekday() == 2

with DAG(dag_id='short_circuit', schedule_interval="@daily", default_args=default_args, tags=['miscellaneous']) as dag:
    
    task_1 = DummyOperator(task_id='dummy_task_1')
    
    task_2 = DummyOperator(task_id='dummy_task_2')

    task_3 = DummyOperator(task_id='dummy_task_3')

    is_wednesday= ShortCircuitOperator(
        task_id='check_for_wednesday',
        python_callable=is_wednesday

    )

    task_4 = DummyOperator(task_id='dummy_task_4')

    task_5 = DummyOperator(task_id='notify', trigger_rule='none_failed')
    
    task_1 >> task_2 >> task_3 >> is_wednesday >> task_4 >> task_5

    task_3 >> task_5
    
    




  