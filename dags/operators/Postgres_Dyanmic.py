from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
import airflow
from airflow.decorators import task

#For this, create a postgres connection in airflow UI with id-postgres, host-postgres,username-airflow,password-airflow

class CustomPostgresOperator(PostgresOperator):
    template_fields =('sql','parameters')

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

@task(task_id="process_user")
def get_email():
    return "jany@gmail.com"


with DAG(dag_id="postgres_dynamic", schedule_interval="@daily", default_args=default_args,tags=['operators']) as dag:
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql="mysql/CREATE_CUSTOMER_TABLE.sql"
        )

    insert_data = CustomPostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres',
        sql='''
            INSERT INTO customers (username,email) VALUES(%(username)s,%(email)s);''',
        parameters = {
            'username': '{{var.value.username}}',
            'email': '{{ti.xcom_pull(task_ids=["process_user"])}}'
        }
        )

    show_values = PostgresOperator(
        task_id='show_data',
        postgres_conn_id='postgres',
        sql='''
            SELECT * FROM sample;'''
        )

    create_table >> get_email() >> insert_data >> show_values    
