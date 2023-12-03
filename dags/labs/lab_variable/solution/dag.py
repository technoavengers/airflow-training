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
    template_fields =('sql','postgres_conn_id')

with DAG(dag_id="variable_sol", schedule_interval="@daily", default_args=default_args,tags=['assignment_solution']) as dag:
    create_table = CustomPostgresOperator(
        task_id='create_table',
        postgres_conn_id='{{var.value.postgres_con}}',
        sql= '{{var.value.mysql}}'
        )

    insert_data = CustomPostgresOperator(
        task_id='insert_data',
        postgres_conn_id='{{var.value.postgres_con}}',
        sql='''
            INSERT INTO employees_oct (name,department,created_at) VALUES('John','HR','{{ds}}');'''
        )



    create_table >> insert_data  