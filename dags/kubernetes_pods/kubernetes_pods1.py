from airflow import DAG
from datetime import datetime
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
                                                          KubernetesPodOperator)
from airflow.configuration import conf
from airflow.decorators import task

import random

# instantiate the DAG
with DAG(
    start_date=datetime(2022,6,1),
    catchup=False,
    schedule_interval='@daily',
    dag_id='Kubernetes_pod_example1',
    tags=['kubernetes']
) as dag:


    testpod1 = KubernetesPodOperator(
        task_id='testpod1',
        image="httpd",
        in_cluster=True,
        namespace='airflow',
        name='my_pod',
        get_logs=True,
        log_events_on_failure=True,
        )
    
    testpod1