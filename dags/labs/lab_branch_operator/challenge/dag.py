import random
from datetime import datetime
import airflow
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.edgemodifier import Label


default_args = {
    "start_date": airflow.utils.dates.days_ago(1),
    'owner': 'Airflow'
}

def choose_branch():
    rand_num = random.randint(0, 2)
    #TODO: Based on above random number, choose the next branch

with DAG (dag_id='branch_operator_assignment', default_args=default_args,
            schedule_interval='@daily', tags=['assignment']) as dag:
    
    first_task = DummyOperator(
        task_id='first_task',
    )

    #TODO: Add a BranchPythonOperator to call python function "choose_branch" to choose next branch
    
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
            #TODO: Add an appropriate trigger_rule
        )
        
        
    #TODO: Add dependencies