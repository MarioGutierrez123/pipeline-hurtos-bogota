from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.append('/opt/airflow/src')
from extract import generar_datos
from transform import transformar_datos

default_args = {
    'owner': 'mario',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='pipeline_hurtos_bogota',
    default_args=default_args,
    description='ETL de hurtos en Bogotá con Faker y PySpark',
    schedule_interval='@daily',
    start_date=datetime(2026, 1, 1),
    catchup=False
) as dag:

    tarea_extract = PythonOperator(
        task_id='extract',
        python_callable=generar_datos
    )

    tarea_transform = PythonOperator(
        task_id='transform',
        python_callable=transformar_datos
    )

    tarea_extract >> tarea_transform
