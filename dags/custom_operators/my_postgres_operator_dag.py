from pendulum import datetime
from airflow import DAG
from custom_operators.my_postgres_operator import MyPostgresOperator


with DAG(dag_id='custom_postgres_operator', schedule='@daily',start_date=datetime(2021, 1, 1),catchup=False) as dag:
 my_postgres_operator = MyPostgresOperator(task_id="dump_table_data",post_conn_id = 'postgres',table= 'dag',file = '/tmp/dags.csv')
 my_postgres_operator