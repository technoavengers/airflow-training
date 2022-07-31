from airflow import DAG
from datetime import datetime
from airflow.operators.sql import BranchSQLOperator
from airflow.operators.dummy import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator


with DAG ('sql_branch_operator', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False,tags=['branch_operator']) as dag:
    
     
     create_table = PostgresOperator(
        task_id='create_table',
        postgres_conn_id='postgres',
        sql='''
            CREATE TABLE IF NOT EXISTS customer (
                firstname TEXT NOT NULL,
                lastname TEXT NOT NULL,
                country TEXT NOT NULL
            );'''
     )
     
     find_customers = BranchSQLOperator(
        task_id="branch_sql",
        conn_id="postgres",
        sql="SELECT count(1) FROM customer",
        follow_task_ids_if_true="customer_exist",
        follow_task_ids_if_false="customer_not_exist",
        dag=dag
        )
    
     customer_exist = DummyOperator(
            task_id='customer_exist',
     )
        
     customer_not_exist = DummyOperator(
            task_id='customer_not_exist',
     )
     
     create_dummy_customer = PostgresOperator(
        task_id='insert_customer',
        postgres_conn_id='postgres',
        sql='''
            INSERT INTO customer (firstname,lastname,country)
            values('Jim','Scandel','US');'''
     )
    
     create_table >> find_customers >> [customer_exist,customer_not_exist]
     
     customer_not_exist >> create_dummy_customer