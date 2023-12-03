from airflow import DAG
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator
import airflow
from airflow.decorators import task

#For this, create a postgres connection in airflow UI with id-postgres, host-postgres,username-airflow,password-airflow

default_args = {
            "owner": "Airflow",
            "start_date": airflow.utils.dates.days_ago(1),
            "depends_on_past": False
        }

//TODO: Create CustomPostgresOperator to extend from PostgresOperator
//TODO: Add sql and postgres_conn_id as template_fields 
class CustomPostgresOperator(PostgresOperator):
    template_fields =('sql','postgres_conn_id')

with DAG(dag_id="variable_assignment", schedule_interval="@daily", default_args=default_args,tags=['assignment']) as dag:
    
    //TODO: Create CustomPostgresOperator task and provide postgres_conn_id, sql as Variable
    //Create SQL Variable with Sql query: “Create table if not exists employees (name varchar(25), department varchar(25),created_at varchar(25))
    //Create postgres connection and put connection name as Variable: host: postgres, username: airflow, password: airflow, host: 5432

    //TODO: Create second task using CustomPostgresOperator
    //INSERT into the above table created_at
    //SQL Query: INSERT INTO employees_oct (name,department,created_at) VALUES('John','HR','{{ds}}');'''

    create_table >> insert_data  
