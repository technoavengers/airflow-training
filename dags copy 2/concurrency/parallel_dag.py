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

with DAG(dag_id="parallel_dag", schedule_interval="@daily", default_args=default_args,tags=['concurrency']) as dag:

    task1 = BashOperator(
            task_id="task1",
            bash_command="sleep 10")

    task2 = BashOperator(
            task_id="task2",
            bash_command="sleep 10")
 
    task3 = BashOperator(
            task_id="task3",
            bash_command="sleep 10")


    task4 = BashOperator(
            task_id="task4",
            bash_command="sleep 10")

    [task1,task2,task3] >> task4