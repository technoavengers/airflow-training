from pendulum import datetime
from airflow import DAG
from custom_operators.my_first_operator import MyOperator


with DAG(dag_id='custom_operator', schedule='@daily',start_date=datetime(2021, 1, 1),catchup=False) as dag:
 custom_operator = MyOperator(task_id="custom_operator",my_parameter ="sample")
 custom_operator