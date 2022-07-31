import sys
import airflow
from airflow import DAG, macros
from airflow.providers.http.operators.http import SimpleHttpOperator
from datetime import datetime, timedelta

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }



with DAG(dag_id="http_operator", schedule_interval="@daily", default_args=default_args,tags=['operators']) as dag:

    extract_user = SimpleHttpOperator(
        task_id='list_user',
        http_conn_id='reqres',
        endpoint='api/users?page=2',
        method='GET',
        log_response=True,
        do_xcom_push=False
    )