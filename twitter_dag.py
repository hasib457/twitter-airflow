from datetime import timedelta, datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from twitter_etl.twitter_etl import twitter_etl

default_args = {
    "owner": "hassib",
    "depend_on_past": False,
    "email": ["haseb457@gmail.com"],
    "emial_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
with DAG(
    "twitter_etl_dag",
    description="simple twitter ETL",
    default_args=default_args,
    schedule=timedelta(days=1),
    start_date=datetime(2022, 12, 10),
    catchup=False,
) as dag:
    etl = PythonOperator(task_id="twitter_etl", python_callable=twitter_etl, dag=dag)
    etl
