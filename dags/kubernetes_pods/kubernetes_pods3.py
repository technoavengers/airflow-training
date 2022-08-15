from airflow import DAG
from datetime import datetime
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
                                                          KubernetesPodOperator)
from airflow.configuration import conf
from airflow.decorators import task
from airflow.operators.bash_operator import BashOperator
import random

# instantiate the DAG
with DAG(
    start_date=datetime(2022,6,1),
    catchup=False,
    schedule_interval='@daily',
    dag_id='Kubernetes_pod_example3',
    tags=['kubernetes']
) as dag:


    write_xcom = KubernetesPodOperator(
        namespace='airflow',
        image='alpine',
        cmds=["sh", "-c", "mkdir -p /airflow/xcom/;echo '[1,2,3,4]' > /airflow/xcom/return.json"],
        name="write-xcom",
        do_xcom_push=True,
        #is_delete_operator_pod=True,
        in_cluster=True,
        task_id="write-xcom",
        get_logs=True,
    )
    
    pod_task_xcom_result = BashOperator(
        bash_command="echo \"pwd\" && echo \"{{ task_instance.xcom_pull('write-xcom')[0] }}\" && sleep 60",
        task_id="pod_task_xcom_result",
    )

    write_xcom >> pod_task_xcom_result