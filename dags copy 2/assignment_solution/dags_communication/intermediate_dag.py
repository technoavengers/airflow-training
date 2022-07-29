import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import task
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import timedelta
from airflow.operators.dagrun_operator import TriggerDagRunOperator

default_args = {
    "start_date": airflow.utils.dates.days_ago(1), 
    "owner": "Airflow"
}


with DAG(dag_id="intermediate_dag", default_args=default_args, schedule_interval="@daily",tags=['dag_communication']) as dag:


    external_task_sensor_task_s3 = ExternalTaskSensor(
        task_id="external_task_sensor_task_s3",
        external_dag_id='parent_dag1',
        external_task_id ='process_file_s3'
        #execution_delta = timedelta(minutes=5)
    )

    trigger_another_dag = TriggerDagRunOperator(
        task_id="test_trigger_dagrun",
        trigger_dag_id="final_dag",
        conf={"message": "Hello World"},
        #execution_date='{{ds}}'
        #reset_dag_run=True
        wait_for_completion=True
    )

    notify_completion  = BashOperator(
        task_id="notify_completion",
        bash_command='echo "All Dags completed"',
    )

    external_task_sensor_task_s3 >> trigger_another_dag >> notify_completion