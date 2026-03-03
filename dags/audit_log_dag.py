from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG("audit_log_archive", start_date=datetime(2024, 1, 1), schedule_interval="@daily", catchup=False) as dag:
    archive = PythonOperator(task_id="archive_logs", python_callable=lambda: print("Archiving audit logs"))
