import airflow
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator



def push_function(**context):
    msg='the_message'
    print("message to push: '%s'" % msg)
    task_instance = context['task_instance']
    task_instance.xcom_push(key="the_message", value=msg)
    

def pull_function(**kwargs):
    ti = kwargs['ti']
    msg = ti.xcom_pull(task_ids='push_task',key='the_message')
    print("received message: '%s'" % msg)

with DAG ('xcom_dag_basic', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False,tags=['xcom']) as dag:


    push_task = PythonOperator(
        task_id='push_task', 
        python_callable=push_function,
        provide_context=True,
        dag=dag)


    pull_task = PythonOperator(
        task_id='pull_task', 
        python_callable=pull_function,
        provide_context=True,
        dag=dag)
    
push_task >> pull_task