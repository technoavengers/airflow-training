from airflow import DAG,Dataset
from airflow.decorators import task

from datetime import datetime

#TODO: Create a Dataset for a file /tmp/file1.csv
#TODO: Create a Dataset for a file /tmp/file2.csv

with DAG (
    dag_id="dataset_consumer_assignment",
    schedule= #TODO: Schedule the dag based on above datasets,
    start_date=datetime(2023,1,1),
    catchup=False,
    tags=['assignment']):
    
    @task
    def read_data():
        with open(file.uri, "r") as f:
            print(f.read())
    
    read_data()