import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.dummy_operator import DummyOperator


default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="triggerdagop_controller_dag", default_args=default_args, schedule_interval="@daily",tags=['trigger_dag_run']) as dag:
    trigger = TriggerDagRunOperator(
        task_id="test_trigger_dagrun",
        trigger_dag_id="trigger_target_dag",
        conf={"message": "Hello World"},
        #execution_date='{{ds}}'
        #reset_dag_run=True
        wait_for_completion=True
    )

    next_task = DummyOperator(task_id="next_task")

    trigger >> next_task