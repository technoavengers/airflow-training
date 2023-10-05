from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from datetime import datetime
import os


default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('spark_application_dag', default_args=default_args, schedule_interval=None)

config_file = os.path.join('C:', 'Users', 'Navdeep', 'config')

volume_mounts = [
    {
        'name': 'jar-volume',  # Choose a meaningful name
        'mountPath': '/opt/spark/app',  # Specify the mount path within the pod
        'subPath': None,  # Use None if you want to mount the entire volume
    }
]

volumes = [
    {
        'name': 'jar-volume',  # Use the same name as in volume_mounts
        'persistentVolumeClaim': {
            'claimName': 'my-pvc',  # Name of the PersistentVolumeClaim (PVC)
        }
    }
]



spark_task = KubernetesPodOperator(
    namespace='default',  # Replace with the appropriate namespace
    image="technoavengers/myspark_image:4.0",  # Docker image of your Spark application
    cmds=["spark-submit"],
    service_account_name='my-spark-sa',
    volume_mounts=volume_mounts,
    volumes=volumes,
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

