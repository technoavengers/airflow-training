import sys
import airflow
from airflow.models import Variable
from airflow import DAG, macros
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

def myfunc(x):
    return x + " Python"


def process(path,file,**context):
    print(f"{path}/{file}-{context['prev_ds']}")


with DAG(dag_id="python_operator", schedule_interval="@daily", default_args=default_args,tags=['operators']) as dag:

    t1 = PythonOperator(
            task_id="task1",
            python_callable=myfunc,
            op_kwargs= {'x':'Welcome'},
            dag= dag)


    t2 = PythonOperator(
            task_id="process_file",
            python_callable=process,
            op_kwargs= {'path':'/opt/data','file':'customers.csv'},
            dag= dag)


    t3 = PythonOperator(
            task_id="template_variables",
            python_callable=process,
            op_kwargs= {'path':'{{var.value.file_path}}','file':'{{var.value.file_name}}'},
            dag= dag)

    t4 = PythonOperator(
            task_id="json_variable",
            python_callable=process,
            op_kwargs= Variable.get("file_settings",deserialize_json=True),
            dag= dag)

    t1 >> t2 >> t3 >> t4