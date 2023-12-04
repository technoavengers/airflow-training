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


with DAG(dag_id="postgres_operator_sensor", schedule_interval="@daily", default_args=default_args,tags=['assignment']) as dag:

    insert_data = PostgresOperator(
        task_id='insert_data',
        postgres_conn_id='postgres',
        sql='''
            INSERT INTO employees_sensor_assignment (id,update_date) VALUES(23,'{{ds}}');'''
        )


    insert_data    
