from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
import airflow

from datetime import datetime, timedelta

default_args = {
    //TODO: Add a start date for yesterday,
    'owner': 'Airflow'
}

//TODO: Create below DAG Object with below details
//dag_id: Report_Analysis
//schedule_interval: Every 30 mins
//tags: ['assignment']

with DAG() as dag:
    
    //TODO: Add a Dummy task with task id "Downlood_Data"

    //TODO: Add a Dummy task with task id "Check_For_Errors"

    //TODO: Add a Dummy task with task id "Notify_For_Errors"

    //TODO: Add a Dummy task with task id "Process"

    //TODO: Add a Dummy task with task id "Save"

    //TODO: Add Task dependencies as shown in assignment


    
    
    




  