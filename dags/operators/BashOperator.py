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

with DAG(dag_id="bash_operator", schedule_interval="@daily", default_args=default_args,tags=['operators']) as dag:

    t1 = BashOperator(
            task_id="make_directory",
            bash_command="mkdir sample",
            dag=dag)

    t2 = BashOperator(
            task_id="create_script",
            bash_command="echo 'pwd' > test.sh &&  chmod +x test.sh && sh test.sh ",
            dag=dag)      

    t1 >> t2