import logging
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

from tempfile import NamedTemporaryFile
from typing import TYPE_CHECKING, Dict, List, Optional, Sequence, Union

from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from custom_operators.my_postgres_operator import MyPostgresOperator


# Change these to your identifiers, if needed.
AWS_S3_CONN_ID = "S3_default"


def s3_upload_fn():
   source_s3_key = "dags.csv"
   source_s3_bucket = "invoices-220161"
   file_path = "/tmp/dags.csv"
   source_s3 = S3Hook(AWS_S3_CONN_ID)
   source_s3.load_file(file_path,source_s3_key,source_s3_bucket)

   	 
with DAG(
	dag_id="postgres_to_s3",
	start_date=datetime(2022, 2, 12),
	schedule_interval=timedelta(days=1),
	catchup=False,
) as dag:


  my_postgres_operator = MyPostgresOperator(task_id="dump_table_data",post_conn_id = 'postgres',table= 'dag',file = '/tmp/dags.csv')
  s3_upload = PythonOperator(
    	task_id="s3_upload",
    	python_callable=s3_upload_fn)
  my_postgres_operator >> s3_upload
