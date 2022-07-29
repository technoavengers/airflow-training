from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.http.sensors.http import HttpSensor
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
from pandas import json_normalize
from airflow.providers.postgres.hooks.postgres import PostgresHook
import json


def _process_user(ti):
    user = ti.xcom_pull(task_ids="extract_user")
    user = user['results'][0]
    processed_user = json_normalize({
        'firstname': user['name']['first'],
        'lastname': user['name']['last'],
        'country': user['location']['country'],
        'username': user['login']['username'],
        'password': user['login']['password'],
        'email': user['email'] })
    processed_user.to_csv('/tmp/processed_user.csv', index=None, header=False)



with DAG ('xcom_dag', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False,tags=['xcom']) as dag:
    
     extract_user = SimpleHttpOperator(
        task_id='extract_user',
        http_conn_id='user_api',
        endpoint='api/',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True,
        #do_xcom_push=False
    )
    
     process_user = PythonOperator(
        task_id='process_user',
        python_callable=_process_user
    )
    
    
     extract_user >> process_user