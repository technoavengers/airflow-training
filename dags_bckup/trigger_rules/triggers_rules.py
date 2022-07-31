# all_success - trigger task when all upstream task succeeds. (default trigger rule) 
# all_failed - trigger task if all upstream task have failed
# all_done - trigger task when all upstream tasks are triggered. It does not depends on status.
# one_success - trigger task as soon as one of the upstream task succeed
# one_failed - trigger task as soon as one of the upstream task faiis
# none_failed - trigger task when all upstream tasks either succeeds or get skipped
# none_failed_or_skipped - triggers tasks when atleast one parent task suceed , other can succeed or skipped 


import random
from datetime import datetime
from airflow.operators.bash_operator import BashOperator

from airflow import DAG

with DAG ('trigger_rules', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False,tags=['trigger_rules']) as dag:
    
    task1 = BashOperator(
        task_id='task1',
        bash_command ='exit 0'
    )
    
    
    task2 = BashOperator(
        task_id='task2',
        bash_command ='exit 0'
    )
    
    task3 = BashOperator(
        task_id='task3',
        bash_command ='exit 0',
        #trigger_rule= 'one_failed'
    )
        
    [task1,task2] >> task3