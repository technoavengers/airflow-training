import random
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.edgemodifier import Label

def choose_branch(execution_date):
    print(execution_date.weekday())
    if execution_date.weekday()==0:
        return 'branch_a'
    if execution_date.weekday()==1:
        return 'branch_b'
    if execution_date.weekday()==4:
        return 'branch_c'


with DAG ('python_branch_operator_assignment', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False,tags=['assignment']) as dag:
    first_task = DummyOperator(
        task_id='first_task',
    )
    
    options = ['branch_a', 'branch_b', 'branch_c']

    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=choose_branch,
    )
    
    
    branch_a = DummyOperator(
            task_id='branch_a',
        )
        
    branch_b = DummyOperator(
            task_id='branch_b',
        )
        
    branch_c = DummyOperator(
            task_id='branch_c',
        )
        
    store = DummyOperator(
            task_id='store',
            trigger_rule='none_failed_or_skipped'
        )
        
        
    first_task >> branching >> [branch_a,branch_b,branch_c] >> store