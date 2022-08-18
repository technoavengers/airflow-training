#Add a taint to node
# kubectl get node
# kubectl label nodes <your-node-name> disktype=ssd
# kubectl get nodes --show-labels

from airflow import DAG
from datetime import datetime
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
                                                          KubernetesPodOperator)
from airflow.configuration import conf
from airflow.decorators import task
from airflow.operators.bash_operator import BashOperator
import random
from kubernetes.client import models as k8s


configmaps = [
    k8s.V1EnvFromSource(config_map_ref=k8s.V1ConfigMapEnvSource(name='test-configmap-1')),
    k8s.V1EnvFromSource(config_map_ref=k8s.V1ConfigMapEnvSource(name='test-configmap-2')),

]

# instantiate the DAG
with DAG(
    start_date=datetime(2022,6,1),
    catchup=False,
    schedule_interval='@daily',
    dag_id='Kubernetes_configmaps',
    tags=['kubernetes']
) as dag:
    
    
    httpd = KubernetesPodOperator(
        task_id='httpd_pod',
        image="httpd",
        in_cluster=True,
        namespace='airflow',
        name='my_pod',
        get_logs=True,
        env_from=configmaps,
        log_events_on_failure=True
    )
    
    httpd


    