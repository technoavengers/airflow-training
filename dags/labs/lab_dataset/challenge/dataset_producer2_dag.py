from airflow import DAG,Dataset
from airflow.decorators import task

from datetime import datetime

#TODO: Create a Dataset for a file /tmp/file2.csv

with DAG (
    dag_id="dataset_producer2_sol",
    schedule="@daily",
    start_date=datetime(2023,1,1),
    catchup=False,
    tags=['assignment']):
    
    #TODO: Write a task to update the above file and indicate the file as outlet of this task
    def update_data():
       #TODO: write the code to append new data into the file
    
    update_data()