from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from datetime import datetime

default_args = {
    'owner': 'your_name',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

dag = DAG('spark_application_dag', default_args=default_args, schedule_interval=None)

spark_task = KubernetesPodOperator(
    namespace='default',  # Replace with the appropriate namespace
    image="technoavengers/myspark_image",  # Docker image of your Spark application
    cmds=["spark-submit"],
    name="spark-task",
    task_id="spark_task",
    get_logs=True,
    dag=dag,
)

spark_task

if __name__ == "__main__":
    dag.cli()

