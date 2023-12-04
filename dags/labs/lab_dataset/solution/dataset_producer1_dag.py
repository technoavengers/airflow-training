from airflow import DAG,Dataset
from airflow.decorators import task

from datetime import datetime

file= Dataset("/tmp/file1.csv")

with DAG (
    dag_id="dataset_producer1_sol",
    schedule="@daily",
    start_date=datetime(2023,1,1),
    catchup=False):
    
    @task(outlets=[file])
    def update_data():
        with open(file.uri, "a+") as f:
            f.write("new data")
    
    update_data()