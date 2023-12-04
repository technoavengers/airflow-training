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
     pg_hook = PostgresHook(postgres_conn_id=postgres_conn)
     pg_hook.bulk_dump(table, file)

     s3_hook = S3Hook(aws_conn_id = s3_connection)
     s3_hook.create_bucket('nav123488884')
     s3_hook.load_file(file,"TEST","nav123488884")


with DAG(dag_id='hooks_sol', schedule_interval='@daily',default_args=default_args,tags=['assignment_solution']) as dag:
 dump_table('postgres_conn','dag_run','/tmp/dag_run.csv','s3_connection') 