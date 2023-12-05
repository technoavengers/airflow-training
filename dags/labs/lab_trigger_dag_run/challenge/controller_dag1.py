import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="triggerdag1", default_args=default_args, schedule_interval="@daily",tags=['assignment_trigger']) as dag:
    
    #TODO: Create a task with TriggerDagRunOperator
    # Call the target dag --> trigger_dag_id="targetdag_assignment",
    # Pass this as conf object to target dag --> conf={"dag_name": "triggerdag1"}

    next_task = DummyOperator(task_id="next_task")

    trigger >> next_task