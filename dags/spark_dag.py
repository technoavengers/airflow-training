from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from datetime import datetime
import os
from kubernetes.client import models as k8s



default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('spark_application_dag', default_args=default_args, schedule_interval=None)

config_file = os.path.join('C:', 'Users', 'Navdeep', 'config')


volume_mount = k8s.V1VolumeMount(
    {'name': 'jar-volume', 'mount_path': '/opt/spark/app', 'sub_path': None, 'read_only': True}
)

volume = k8s.V1Volume(
   {'name':'jar-volume',
    'persistent_volume_claim':k8s.V1PersistentVolumeClaimVolumeSource(claim_name="my-pvc")}
)



spark_task = KubernetesPodOperator(
    namespace='default',  # Replace with the appropriate namespace
    image="technoavengers/myspark_image:4.0",  # Docker image of your Spark application
    cmds=["spark-submit"],
    service_account_name='my-spark-sa',
    volume_mounts=volume_mount,
    volumes=volume,
    arguments=[
        '--class', 'InMemoryDataset',
        '--master', 'k8s://https://kubernetes.default.svc:443',
        '--deploy-mode', 'cluster',
        '--conf', 'spark.executor.instances=2',  # Set the desired number of executors
        '--conf', 'spark.kubernetes.authenticate.driver.serviceAccountName=my-spark-sa',
        '--conf', 'spark.kubernetes.driver.container.image=technoavengers/myspark_image:4.0',
        '--conf', 'spark.kubernetes.container.image=technoavengers/myspark_image:4.0',
        '--conf','spark.kubernetes.file.upload.path=/opt/spark/temp',
        '--files', '/opt/spark/app/myspark.jar',
        '/opt/spark/app/myspark.jar'
    ],
    name="spark-task",
    task_id="spark_task",
    get_logs=True,
    dag=dag,
)

spark_task

if __name__ == "__main__":
    dag.cli()

