from airflow import DAG
from airflow.decorators import task
from airflow.utils.dates import days_ago

with DAG(
    "dag-3",
    schedule=None,
    start_date=days_ago(1),
    catchup=False
) as dag:

    @task
    def taski():
        print("Task i executed")

    @task
    def taskii():
        print("Task ii executed")

    taski() >> taskii()
