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

affinity = k8s.V1Affinity(
    node_affinity=k8s.V1NodeAffinity(
        preferred_during_scheduling_ignored_during_execution=[
            k8s.V1PreferredSchedulingTerm(
                weight=1,
                preference=k8s.V1NodeSelectorTerm(
                    match_expressions=[
                        k8s.V1NodeSelectorRequirement(key="disktype", operator="In", values=["ssd"])
                    ]
                ),
            )
        ]
))

tolerations = [k8s.V1Toleration(key="gpu", operator="Equal", value="available")]
# instantiate the DAG
with DAG(
    start_date=datetime(2022,6,1),
    catchup=False,
    schedule_interval='@daily',
    dag_id='Kubernetes_tolerations',
    tags=['kubernetes']
) as dag:
    
    
    httpd = KubernetesPodOperator(
        task_id='httpd_pod',
        image="httpd",
        in_cluster=True,
        namespace='airflow',
        name='my_pod',
        get_logs=True,
        affinity=affinity,
        tolerations=tolerations,
        log_events_on_failure=True
    )
    
    httpd


    