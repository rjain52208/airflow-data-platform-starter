"""
Example daily ETL pipeline for the Airflow data platform.

This DAG simulates:
- extracting data from a CSV "source"
- transforming/cleaning it
- loading it into a target table

It is meant to demonstrate pipeline structure, not real business logic.
"""

from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator


def extract(**context):
    # In a real project, you would read from S3/API/DB.
    # Here we just log to show the task ran.
    print("Extracting raw data from source...")
    # You could push XComs here if needed.


def transform(**context):
    # In a real project, you would clean, filter, or aggregate data.
    print("Transforming data (cleaning, type casting, etc.)...")


def load(**context):
    # In a real project, you would write to a warehouse table (PostgreSQL/Redshift/etc.).
    print("Loading data into analytics table...")


default_args = {
    "owner": "riddhi_jain",
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="example_daily_etl",
    description="Daily example ETL pipeline for the Airflow data platform",
    default_args=default_args,
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["etl", "example", "data-platform"],
) as dag:
    extract_task = PythonOperator(
        task_id="extract_raw_data",
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=transform,
    )

    load_task = PythonOperator(
        task_id="load_into_target",
        python_callable=load,
    )

    # Define task dependencies: extract -> transform -> load
    extract_task >> transform_task >> load_task
