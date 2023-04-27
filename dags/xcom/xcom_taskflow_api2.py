import airflow
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import task

@task(task_id="extract")
def extract_fn():
    return 'welcome'

@task(task_id="transform1")
def transform1_fn(value_from_extract):
    print("received message: '%s'" % value_from_extract)
    
@task(task_id="transform2")
def transform2_fn(value_from_extract):
    print("received message: '%s'" % value_from_extract)

with DAG ('xcom_dag_basic_taskflow_1', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False,tags=['xcom']) as dag:
    
    transform1_fn(extract_fn())
    transform2_fn(extract_fn())