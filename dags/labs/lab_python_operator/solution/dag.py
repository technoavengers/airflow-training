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

def add(x,y):
    return x + y

@task(task_id="multiply")
def multiply_fn(x,y):
    return x * y


with DAG(dag_id="python_operator_sol", schedule_interval="@daily", default_args=default_args,tags=['assignment_solution']) as dag:

    add_task = PythonOperator(
            task_id="add",
            python_callable=add,
            op_kwargs={"x": 3, "y": 4})


    add_task >> multiply_fn(3,4)