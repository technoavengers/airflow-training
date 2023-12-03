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

def random_generator(ti):
    msg=random.random()
    #TODO: Push random number generated above in a xcom with key "random"
    #TODO: Pull an xcom produced by previous task "Http_generator" and print it
    

def print_random(ti):
    #TODO: Pull the random number pushed in Xcom in previoys task "random_generator"
    #TODO: Print the random number

    

with DAG ('xcom_assignment', default_args=default_args,
            schedule_interval='@daily', catchup=False,tags=['assignment']) as dag:

    #TODO: Add SimpleHttpOperator as given in assignment

    #TODO: Add PythonOperator to call "random_generator" function

    #TODO: Add PythonOperator to call "print_random" function
  
    #TODO: Add dependencies 
