import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="triggerdag2_sol", default_args=default_args, schedule_interval="@daily",tags=['assignment_trigger']) as dag:
    trigger = TriggerDagRunOperator(
        task_id="test_trigger_dagrun",
        trigger_dag_id="targetdag_sol",
        conf={"dag_name": "triggerdag2"},
    )

    next_task = DummyOperator(task_id="next_task")

    trigger >> next_task