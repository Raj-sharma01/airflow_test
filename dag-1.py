from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago

with DAG(
    "dag_1",
    schedule=None,
    start_date=days_ago(1),
    catchup=False
) as dag:

    @task
    def task1():
        print("Task 1 executed")

    @task
    def task2():
        print("Task 2 executed")

    task1() >> task2()
