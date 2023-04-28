import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import task
from airflow.sensors.external_task import ExternalTaskSensor
from datetime import timedelta
from airflow.models import DagRun
from airflow import AirflowException

default_args = {
    "start_date": airflow.utils.dates.days_ago(1), 
    "owner": "Airflow"
}

def get_custom_date(execution_date,**kwargs):
    dag_runs = DagRun.find(dag_id='external_sensor_parent_dag_s3')
    dag_runs.sort(key=lambda x: x.execution_date, reverse=True)
    latest_dag_run = dag_runs[0] if dag_runs else None
    print(dag_runs[0].get_state())
    if latest_dag_run is not None and latest_dag_run.get_state()== 'success':
        return latest_dag_run.execution_date
    else:
        raise AirflowException("Last DagRun was not successful or not found") 


with DAG(dag_id="external_sensor_target_dag", default_args=default_args, schedule_interval="@daily",tags=['external_task_sensor']) as dag:


    external_task_sensor_task_s3 = ExternalTaskSensor(
        task_id="external_task_sensor_task_s3",
        external_dag_id='external_sensor_parent_dag_s3',
        external_task_id ='process_file_s3',
        #execution_delta = timedelta(minutes=5)
        execution_date_fn = get_custom_date
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