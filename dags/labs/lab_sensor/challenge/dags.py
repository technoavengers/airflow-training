import airflow
from pendulum import datetime
from airflow import DAG
from airflow.decorators import task
from airflow.sensors.sql import SqlSensor
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1)
}


with DAG(dag_id='sql_sensor_assignment', schedule_interval='@daily',default_args=default_args,tags=['assignment']) as dag:
     
     create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql="CREATE TABLE IF NOT EXISTS employees_sensor_assignment (id varchar(25),update_date varchar(25))"
        )

    #TODO: Write SqlSensor to check for count in employees_sensor_assignment for execution date
    #TODO: sql="Select count(*) from employees_sensor where update_date='{{ds}}'",
    #TODO: poke_interval=10,
    #TODO: timeout=150,

     
     t2 = DummyOperator(task_id="task1")
     
     create_table >> t1 >> t2
