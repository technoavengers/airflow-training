import sys
import airflow
from airflow.models import Variable
from airflow import DAG, macros
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.decorators import task
from airflow.operators.bash_operator import BashOperator

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }


@task(task_id="process_files")
def process(file_settings,**context):
    print(f"{file_settings['path']}/{file_settings['file']}-{context['ds']}")


with DAG(dag_id="python_task_flow", schedule_interval="@daily", default_args=default_args,tags=['operators']) as dag:

    t1 = BashOperator(
            task_id="make_directory",
            bash_command="mkdir sample",
            dag=dag)
    
    t1 >> process(Variable.get("file_settings",deserialize_json=True))