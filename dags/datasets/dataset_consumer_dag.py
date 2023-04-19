from airflow import DAG,Dataset
from airflow.decorators import task

from datetime import datetime

file= Dataset("/tmp/new_file.csv")

with DAG (
    dag_id="dataset_consumer",
    schedule= [file],
    start_date=datetime(2023,1,1),
    catchup=False):
    
    @task
    def read_data():
        with open(file.uri, "r") as f:
            print(f.read())
    
    read_data()