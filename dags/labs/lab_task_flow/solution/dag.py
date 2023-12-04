import sys
import airflow
from airflow.models import Variable
from airflow import DAG, macros
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from airflow.decorators import task

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

@task(task_id="add")
def add_fn(x,y):
    return x + y

@task(task_id="multiply")
def multiply_fn(x,y):
    return x * y


with DAG(dag_id="task_flow_sol", schedule_interval="@daily", default_args=default_args,tags=['assignment_solution']) as dag:


    add_fn(3,4) >> multiply_fn(3,4)