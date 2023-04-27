import random
from datetime import datetime

from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.edgemodifier import Label

def choose_rand_branch():
    a=random.randint(1,3)
    print("random value is: '%s'" % a)
    if a==1:
        return 'branch_a'
    if a==2:
        return 'branch_b'
    if a==3:
        return 'branch_c'


with DAG ('branch_operator_assignment', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False,tags=['assignment']) as dag:
    Download = DummyOperator(
        task_id='Download',
    )
    
    options = ['branch_a', 'branch_b', 'branch_c']

    choose_branch = BranchPythonOperator(
        task_id='choose_branch',
        python_callable=choose_rand_branch,
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
        
    report = DummyOperator(
            task_id='report',
            trigger_rule='none_failed_or_skipped'
        )
        
        
    Download >> choose_branch >> [branch_a,branch_b,branch_c] >> report