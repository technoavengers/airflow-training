import airflow
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import task



@task(task_id="push_task")
def push_function(**kwargs):
    ti = kwargs["ti"]
    ti.xcom_push(key="color", value='red')
    return 'welcome'
    
@task(task_id="pull_task")
def pull_function(value_from_task1,**kwargs):
    ti = kwargs["ti"]
    color = ti.xcom_pull(task_ids='push_task',key='color')
    print(color)
    print("received message: '%s'" % value_from_task1)



with DAG ('xcom_dag_basic_taskflow', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False,tags=['xcom']) as dag:
    
    pull_function(push_function()) 
