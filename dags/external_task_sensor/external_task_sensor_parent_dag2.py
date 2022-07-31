import pprint as pp
import airflow.utils.dates
from airflow import DAG
from airflow.operators.dagrun_operator import TriggerDagRunOperator
from airflow.operators.bash_operator import BashOperator


default_args = {
        "owner": "airflow", 
        "start_date": airflow.utils.dates.days_ago(1)
    }

with DAG(dag_id="external_sensor_parent_dag_http", default_args=default_args, schedule_interval="@daily",tags=['external_task_sensor']) as dag:
    

    download_file_http = BashOperator(
        task_id="download_file_http",
        bash_command='echo "Downloading File from Http" && sleep 60',
    )


    process_file_http  = BashOperator(
        task_id="process_file_http",
        bash_command='echo "Process file from Http"',
    )

    download_file_http >> process_file_http