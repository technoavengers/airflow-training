import sys
import airflow
from airflow import DAG, macros
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

with DAG(dag_id="bash_operator1", schedule_interval="@hourly", default_args=default_args,tags=['operators']) as dag:


    t1 = BashOperator(
            task_id="make_directory",
            bash_command="mkdir sample",
            dag=dag)

    for i in range(3):
        i = str(i)
        task = BashOperator(
            task_id='runme_'+i,
            bash_command='echo "{{ task_instance_key_str }}" && sleep 15',
            dag=dag)
        task.set_downstream(t1) 