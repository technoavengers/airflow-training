import sys
import airflow
from airflow import DAG, macros
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta
import json
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

class CustomPostgresOperator(PostgresOperator):
    template_fields =('sql','parameters')

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

def _process_user(ti):
    ti.xcom_pull
    # Pull out xcom from task get_user
    user_data = str(user['data'])
    user_data = user_data.replace("\'", "\"")
    user_dict =  json.loads(user_data)
    # Push xcomm variable with key firstname
    # Push xcom variable with key 
    # Push xcom variable with key email


with DAG(dag_id="assignment_solution", schedule_interval="@daily", default_args=default_args,tags=['assignment']) as dag:

    get_user = SimpleHttpOperator(
        task_id='get_user',
        http_conn_id='reqres',  #create a connection in airflow ui
        endpoint='api/users/2',
        method='GET',
        response_filter=lambda response: json.loads(response.text),
        log_response=True
    )

    process_user = PythonOperator(
        task_id='process_user',
        python_callable=_process_user
    )

    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql= #Use Airflow Variables to write sql query to create users table with firstname,lastname and email
    )

    insert_data = CustomPostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres',
        sql= # write sql query to insert into user table, set dynamic parameters
        parameters = {
            'firstname': #pull xcom variable firstname from your python task,
            'lastname': #pull xcom variable lastname from your python task,
            'email': #pull xcom variable lastname from your python task
        }
        )

    get_user >> process_user >> create_table >> insert_data