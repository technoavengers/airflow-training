import airflow
from pendulum import datetime
from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.S3_hook import S3Hook
from airflow.decorators import task

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1)
}

@task
def dump_table(postgres_conn,table,file,s3_connection):
     #TODO: Create a Postgres Hook from postgres connection
     #TODO: Use postgres Hook - bulk_dump method to dump table into file


     #TODO: Create a S3Hook from S3 Connection
     #TODO: Use S3Hook - create_bucket to create a S3 bucket
     #TODO: Use S3Hook - Use load_file method to load file into S3 Buckt




with DAG(dag_id='hooks_assignment', schedule_interval='@daily',,default_args=default_args,tags=['assignment']) as dag:
     dump_table('postgres_conn','dag_run','/tmp/dag_run.csv','s3_connection') 