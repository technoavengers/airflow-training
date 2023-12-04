import airflow
from datetime import datetime, timedelta
from airflow import DAG
from custom_sensors.file_sql_sensor import CustomFileAndSQLSensor

default_args = {
    "owner": "Airflow",
    "start_date": airflow.utils.dates.days_ago(1)
}

dag = DAG('file_sql_sensor_dag', default_args=default_args, schedule_interval='@daily')

file_and_sql_sensor_task = CustomFileAndSQLSensor(
        task_id='file_and_sql_sensor_task',
        filepath='/tmp/invoice.csv',
        sql_query="Select * from employees_sensor where id='23'",
        dag=dag,
    )

file_and_sql_sensor_task