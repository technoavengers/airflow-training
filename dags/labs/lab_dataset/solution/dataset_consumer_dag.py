from airflow import DAG,Dataset
from airflow.decorators import task

from datetime import datetime

file1= Dataset("/tmp/file1.csv")
file2= Dataset("/tmp/file1.csv")

with DAG (
    dag_id="dataset_consumer_sol",
    schedule= [file1,file2],
    start_date=datetime(2023,1,1),
    catchup=False):
    
    @task
    def read_data():
        with open(file.uri, "r") as f:
            print(f.read())
    
    read_data()