import sys
import airflow
from airflow.models import Variable
from airflow import DAG, macros
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

class CustomPostgresOperator(PostgresOperator):
    template_fields =('sql','parameters')


with DAG(dag_id="postgres_Custom_operator", schedule_interval="@daily", default_args=default_args,tags=['operators']) as dag:
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql= '{{var.value.create_sql}}'
        )

    insert_data = CustomPostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres',
        sql='''
            INSERT INTO
 employees (name,department,created_at) VALUES(%(name)s,%(department)s,%(created_at)s);''',
        parameters = {
            'name': '{{var.value.name}}',
            'department': '{{var.value.department}}',
            'created_at': '{{ds}}'
        }
        )

    show_data = PostgresOperator(
        task_id='show_data',
        postgres_conn_id='postgres',
        sql='''
            SELECT * FROM employees;'''
        )

    create_table >> insert_data >> show_data