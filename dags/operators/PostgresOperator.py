from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
import airflow
from airflow.decorators import task

#For this, create a postgres connection in airflow UI with id-postgres, host-postgres,username-airflow,password-airflow

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

class CustomPostgresOperator(PostgresOperator):
    template_fields =('sql','parameters')

@task(task_id="generate_id")
def generate_id():
    return 23

with DAG(dag_id="postgres_operator", schedule_interval="@daily", default_args=default_args,tags=['operators']) as dag:
    create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql="mysql/CREATE_TABLE.sql"
        )

    insert_data = CustomPostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres',
        sql='''
            INSERT INTO sample123 (id) VALUES(23);'''
        #parameters = {
        #    'id': '{{ti.xcom_pull(task_ids=["generate_id"])}}'
        #}
        )

    show_values = PostgresOperator(
        task_id='show_data',
        postgres_conn_id='postgres',
        sql='''
            SELECT * FROM sample123;'''
        )

    create_table >> insert_data >> show_values    
