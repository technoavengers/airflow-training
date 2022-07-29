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
    user = ti.xcom_pull(task_ids="get_user")
    user_data = str(user['data'])
    user_data = user_data.replace("\'", "\"")
    user_dict =  json.loads(user_data)
    ti.xcom_push(key="firstname", value=user_dict['first_name'])
    ti.xcom_push(key="lastname", value=user_dict['last_name'])
    ti.xcom_push(key="email", value=user_dict['email'])


with DAG(dag_id="assignment_solution", schedule_interval="@daily", default_args=default_args,tags=['assignment']) as dag:

    get_user = SimpleHttpOperator(
        task_id='get_user',
        http_conn_id='reqres',
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
        sql='{{var.value.Create_sql}}'
    )

    insert_data = CustomPostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres',
        sql='''
            INSERT INTO users (firstname,lastname,email) VALUES(%(firstname)s,%(lastname)s,%(email)s);''',
        parameters = {
            'firstname': '{{ti.xcom_pull(task_ids=["process_user"],key="firstname")}}',
            'lastname': '{{ti.xcom_pull(task_ids=["process_user"],key="lastname")}}',
            'email': '{{ti.xcom_pull(task_ids=["process_user"],key="email")}}'
        }
        )


    get_user >> process_user >> create_table >> insert_data