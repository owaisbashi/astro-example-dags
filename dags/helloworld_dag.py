from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

# Define default_args dictionary to pass to the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Instantiate a DAG
dag = DAG(
    'helloworld_dag',
    default_args=default_args,
    description='A simple DAG for Hello, World!',
    schedule_interval=timedelta(days=1),  # Adjust the interval as needed
)

# Define the Python function to be executed
def hello_world():
    print("Hello, World!")

# Create a PythonOperator that calls the hello_world function
hello_task = PythonOperator(
    task_id='hello_task',
    python_callable=hello_world,
    dag=dag,
)

# Set the task dependencies (if any)
# For this simple DAG, there are no dependencies

# Define the task execution order
hello_task
