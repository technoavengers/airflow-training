import airflow
from datetime import datetime, timedelta
from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator



def push_function(ti):
    msg='the_message'
    print("message to push: '%s'" % msg)
    #task_instance = context['task_instance']
    ti.xcom_push(key="xcom1", value='xcom1_value')
    ti.xcom_push(key="xcom2", value='xcom2_value')
    return 'Welcome to XCOM'
    

def pull_function(ti):
    msg = ti.xcom_pull(task_ids='push_task',key='xcom1')
    print("received message: '%s'" % msg)
    
def pull_function2(ti):
    msg = ti.xcom_pull(task_ids='push_task',key='xcom2')
    print("received message: '%s'" % msg)
    
def pull_function3(ti):
    msg = ti.xcom_pull(task_ids='push_task')
    print("default xcom is recieved: '%s'" % msg)

with DAG ('xcom_dag_basic', start_date=datetime(2022,1,1),
            schedule_interval='@daily', catchup=False,tags=['xcom']) as dag:


    push_task = PythonOperator(
        task_id='push_task', 
        python_callable=push_function,
        provide_context=True,
        dag=dag)


    pull_task = PythonOperator(
        task_id='pull_task', 
        python_callable=pull_function,
        provide_context=True,
        dag=dag)
        
        
    pull_task2 = PythonOperator(
        task_id='pull_task2', 
        python_callable=pull_function2,
        provide_context=True,
        dag=dag)
        
    pull_task3 = PythonOperator(
        task_id='pull_task3', 
        python_callable=pull_function3,
        provide_context=True,
        dag=dag)
    
    push_task >> pull_task >> pull_task2 >> pull_task3