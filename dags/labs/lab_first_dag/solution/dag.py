from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
import airflow

from datetime import datetime, timedelta

default_args = {
    "start_date": airflow.utils.dates.days_ago(1),
    'owner': 'Airflow'
}

with DAG(dag_id= "report_analysis_sol", schedule_interval="0/30 * * * *", default_args=default_args, tags=['assignment_solution']) as dag:
    
    task_1 = DummyOperator(task_id='Download_Data')
    
    task_2 = DummyOperator(task_id='Check_For_Errors')

    task_3 = DummyOperator(task_id='Notify_For_Errors')

    task_4 = DummyOperator(task_id='Process')

    task_5 = DummyOperator(task_id='Save')

    
    task_1 >> task_2 >> [task_3,task_4] >> task_5



  