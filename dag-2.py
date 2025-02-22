from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago

with DAG(
    "dag_2",
    schedule=None,
    start_date=days_ago(1),
    catchup=False
) as dag:

    @task
    def taskA():
        print("Task A executed")

    @task
    def taskB():
        print("Task B executed")

    taskA() >> taskB()
