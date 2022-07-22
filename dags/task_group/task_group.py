from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.task_group import TaskGroup
 
from datetime import datetime
 
with DAG('task_group', start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False,tags=['task_group']) as dag:
 
    
    with TaskGroup ('download_files') as download_files:
        download_file1 = BashOperator(
        task_id='Download_file1',
        bash_command='sleep 1'
        )
 
        download_file1 = BashOperator(
        task_id='Download_file2',
        bash_command='sleep 1'
        )
 
    check_files = BashOperator(
        task_id='Check_files',
        bash_command='sleep 1'
    )
    
    with TaskGroup ('process_files') as process_files:
        process_file1 = BashOperator(
        task_id='Process_file1',
        bash_command='sleep 1'
        )
 
        process_file2 = BashOperator(
        task_id='Process_file2',
        bash_command='sleep 1'
        )
        
    with TaskGroup ('store_files') as store_files:
        with TaskGroup ('store_mysql') as store_mysql:
            store_file1= BashOperator(
            task_id='store_file1',
            bash_command='sleep 1'
            )
            store_file2 = BashOperator(
            task_id='store_file2',
            bash_command='sleep 1'
            )
        
        with TaskGroup ('store_cassandra') as store_cassandra:
            store_file1= BashOperator(
            task_id='store_file1',
            bash_command='sleep 1'
            )
            store_file2 = BashOperator(
            task_id='store_file2',
            bash_command='sleep 1'
            )
 
        
 
    download_files >> check_files >> process_files >> store_files