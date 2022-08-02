import random
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.weekday import BranchDayOfWeekOperator

with DAG ('week_branch_operator', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False, tags=['branch_operator']) as dag:
    
    branch = BranchDayOfWeekOperator(
        task_id="branch_week_choice",
        follow_task_ids_if_true="branch_tuesday",
        follow_task_ids_if_false="branch_others",
        week_day="Tuesday",
    )
    
    
    branch_tuesday = DummyOperator(
            task_id='branch_tuesday',
        )
        
    branch_others = DummyOperator(
            task_id='branch_others',
        )
        
    notify = DummyOperator(
            task_id='notify_users',
        )
        
        
    branch >> [branch_tuesday,branch_others] >> notify