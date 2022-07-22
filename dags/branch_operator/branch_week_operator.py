import random
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.weekday import BranchDayOfWeekOperator

with DAG ('week_branch_operator', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False, tags=['branch_operator']) as dag:
    
    branch = BranchDayOfWeekOperator(
        task_id="branch_week_choice",
        follow_task_ids_if_true="branch_monday",
        follow_task_ids_if_false="branch_others",
        week_day="Monday",
    )
    
    
    branch_monday = DummyOperator(
            task_id='branch_monday',
        )
        
    branch_others = DummyOperator(
            task_id='branch_others',
        )
        
        
    branch >> [branch_monday,branch_others]