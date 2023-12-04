import airflow
from pendulum import datetime
from airflow import DAG
from labs.lab_custom_operator.solution.custom_add_operator import AddOperator


default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1)
}

with DAG(dag_id='custom_operator_sol', schedule='@daily',default_args=default_args,tags=['assignment_solution']) as dag:
 custom_operator = AddOperator(task_id="custom_operator",num1 = 1, num2 = 2)
 custom_operator