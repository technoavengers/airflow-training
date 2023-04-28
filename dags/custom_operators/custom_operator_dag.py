from pendulum import datetime
from airflow import DAG
from custom_operators.my_first_operator import MyOperator


# AKIAWDDNL5XOY2Q4K7LP
# MuL5cjd88vi+DQDjJq7mWf1KYgfaaqDD9c+c9Y0r

with DAG(dag_id='custom_operator', schedule='@daily',start_date=datetime(2021, 1, 1),catchup=False) as dag:
 custom_operator = MyOperator(task_id="custom_operator",name ="navdeep")
 custom_operator