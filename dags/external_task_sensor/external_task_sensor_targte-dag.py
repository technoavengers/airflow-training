import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import task
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import timedelta

default_args = {
    "start_date": airflow.utils.dates.days_ago(1), 
    "owner": "Airflow"
}


with DAG(dag_id="external_sensor_target_dag", default_args=default_args, schedule_interval="@daily",tags=['external_task_sensor']) as dag:


    external_task_sensor_task_s3 = ExternalTaskSensor(
        task_id="external_task_sensor_task_s3",
        external_dag_id='external_sensor_parent_dag_s3',
        external_task_id ='process_file_s3'
        #execution_delta = timedelta(minutes=5)
    )

    external_task_sensor_task_http = ExternalTaskSensor(
        task_id="external_task_sensor_task_http",
        external_dag_id='external_sensor_parent_dag_http',
        external_task_id ='process_file_http'
    )

    notify_completion  = BashOperator(
        task_id="notify_completion",
        bash_command='echo "All Dags completed"',
    )

    [external_task_sensor_task_s3,external_task_sensor_task_http] >>  notify_completion