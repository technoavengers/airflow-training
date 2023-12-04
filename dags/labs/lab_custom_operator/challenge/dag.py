from pendulum import datetime
from airflow import DAG
from labs.lab_custom_operator.challenge.add_operator import AddOperator

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1)
}

with DAG(dag_id='custom_operator_assignment', schedule='@daily',default_args=default_args,tags=['assignment']) as dag:
 #TODO: Create a task for  Add Operator and pass num1 and num2 as parameter
 #TODO: Add dependencies to call the operator