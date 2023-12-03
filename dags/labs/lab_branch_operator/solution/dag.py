import random
import airflow
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.edgemodifier import Label

default_args = {
    "start_date": airflow.utils.dates.days_ago(1),
    'owner': 'Airflow'
}

def choose_branch(execution_date):
    msg = random.randint(0, 2)
    print("message received from Http_generator task is '%s'" %msg)
    if msg==0:
        return 'branch_0'
    if msg==1:
        return 'branch_1'
    if msg==2:
        return 'branch_2'

with DAG (dag_id='branch_operator_sol', default_args=default_args,
            schedule_interval='@daily', tags=['assignment_solution']) as dag:
    
    first_task = DummyOperator(
        task_id='first_task',
    )

    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=choose_branch,
    )
    
    
    branch_0 = DummyOperator(
            task_id='branch_0',
        )
        
    branch_1 = DummyOperator(
            task_id='branch_1',
        )
        
    branch_2 = DummyOperator(
            task_id='branch_2',
        )
        
    save = DummyOperator(
            task_id='save',
            trigger_rule='none_failed_or_skipped'
        )
        
        
    first_task >> branching >> [branch_0,branch_1,branch_2] >> save