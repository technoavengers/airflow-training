import airflow
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.providers.http.operators.http import SimpleHttpOperator
import random

default_args = {
    "start_date": airflow.utils.dates.days_ago(1),
    'owner': 'Airflow'
}

def Random_generator(ti):
    msg=random.random()
    print("random number to push: '%s'" % msg)
    #task_instance = context['task_instance']
    ti.xcom_push(key="random", value=msg)
    json_value=ti.xcom_pull(task_ids='Http_generator',key='return_value')
    print("message received from Http_generator task is '%s'" %json_value)
    return 'JSON printed and random number pushed to XCOM'
    

def print_random(ti):
    random = ti.xcom_pull(task_ids='Random_generator',key='random')
    print("received number received from Random_generator: '%s'" % random)

    

with DAG (dag_id='xcom_assignment_sol', default_args=default_args,
            schedule_interval='@daily', catchup=False,tags=['assignment_solution']) as dag:

    Http_generator = SimpleHttpOperator(
        task_id='Http_generator',
        http_conn_id='reqres',
        endpoint='api/users?page=2',
        method='GET',
        log_response=True
    )

    Random_generator = PythonOperator(
        task_id='Random_generator', 
        python_callable=Random_generator,
        provide_context=True,
        dag=dag)


    print_random = PythonOperator(
        task_id='print_random', 
        python_callable=print_random,
        provide_context=True,
        dag=dag)
        

    
    Http_generator >> Random_generator >> print_random