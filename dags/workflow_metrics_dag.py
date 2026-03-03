from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from tasks.extract import extract_workflow_data
from tasks.transform import transform_metrics
from tasks.load import load_to_warehouse

with DAG("workflow_metrics", start_date=datetime(2024, 1, 1), schedule_interval="@hourly", catchup=False, default_args={"retries": 3, "retry_delay": timedelta(minutes=5)}) as dag:
    extract = PythonOperator(task_id="extract", python_callable=extract_workflow_data)
    transform = PythonOperator(task_id="transform", python_callable=transform_metrics)
    load = PythonOperator(task_id="load", python_callable=load_to_warehouse)
    extract >> transform >> load
