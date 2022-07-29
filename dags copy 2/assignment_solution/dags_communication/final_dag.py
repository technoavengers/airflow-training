import airflow.utils.dates
from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.decorators import task

default_args = {
    "start_date": airflow.utils.dates.days_ago(1), 
    "owner": "Airflow"
}

@task(task_id="run_this")
def run_this_func(dag_run=None):
    """
    Print the payload "message" passed to the DagRun conf attribute.
    :param dag_run: The DagRun object
    """
    print(f"Remotely received value of {dag_run.conf.get('message')} for key=message")


with DAG(dag_id="final_dag", default_args=default_args, schedule_interval=None,tags=['dag_communication']) as dag:

    run_this = run_this_func()

    bash_task = BashOperator(
        task_id="bash_task",
        bash_command='echo "Here is the message: $message" && sleep 10',
        env={'message': '{{ dag_run.conf.get("message") }}'},
    )

    bash_task >> run_this