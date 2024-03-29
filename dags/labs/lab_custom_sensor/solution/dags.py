import airflow
from datetime import datetime, timedelta
from airflow import DAG
from labs.lab_custom_sensor.solution.custom_file_s3_sensor import CustomFileAndS3Sensor

default_args = {
    "owner": "Airflow",
    "start_date": airflow.utils.dates.days_ago(1)
}

dag = DAG('file_s3_sensor_solution', default_args=default_args, schedule_interval='@daily')

file_and_s3_sensor_task = CustomFileAndS3Sensor(
        task_id='file_and_s3_sensor_task',
        filepath='/tmp/invoice1.csv',
        s3_bucket='s3sensorbucketairflow',
        s3_conn_id='s3_conn',
        s3_key='ratings_new.csv',
        dag=dag,
    )

file_and_s3_sensor_task