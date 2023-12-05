import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import task
from airflow.operators.python import BranchPythonOperator
from airflow.operators.dummy_operator import DummyOperator

default_args = {
    "start_date": airflow.utils.dates.days_ago(1), 
    "owner": "Airflow"
}

def choose_branch(dag_run=None):
    #TODO: Write logic to get dag_name out of this dag_run object
    # if dag_name= triggerdag1, go to dag1_branch
    # if dag_name = triggerdag2, go to dag2_branch

with DAG(dag_id="targetdag", default_args=default_args, schedule_interval=None,tags=['assignment_trigger']) as dag:

    branching = BranchPythonOperator(
        task_id='branching',
        python_callable=choose_branch,
    )
    
    
    dag1_branch = DummyOperator(
            task_id='dag1_branch',
        )
        
    dag2_branch = DummyOperator(
            task_id='dag2_branch',
        )
    
    store = DummyOperator(
            task_id='store',
            trigger_rule='none_failed_or_skipped'
        )
        
        
    branching >> [dag1_branch,dag2_branch] >> store