from airflow import DAG
from datetime import datetime
from custom_hooks.custom_api_hook import CustomApiHook # Import your custom hook
from airflow.decorators import task

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
}

@task(task_id="call_custom_hook")
def custom_hook_fn():
    api_hook = CustomApiHook(custom_api_conn_id='reqres')
    # Example: Fetch data from an API using the custom hook
    endpoint_data = api_hook.get_data('api/users/2')
    print(endpoint_data) # Do something with the response data
    


with DAG('custom_hook_example', default_args=default_args, schedule_interval='@daily',catchup=False) as dag:
    custom_hook_fn()