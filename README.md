# Pipeline Hurtos Bogotá

> Pipeline ETL con datos simulados de hurtos en Bogotá | ETL pipeline simulating theft data in Bogotá

## 📌 Descripción
Proyecto ETL end-to-end que simula, procesa y analiza datos de hurtos en Bogotá. Diseñado para demostrar habilidades de Ingeniería de Datos solicitadas en vacantes bilingües.

## 🛠️ Tech Stack
- **Lenguaje:** Python, PySpark, SQL
- **Orquestación:** Apache Airflow (DAG)
- **Cloud:** Google Cloud Platform (Dataproc, BigQuery)
- **Librerías:** Pandas, Faker, Matplotlib
- **Control de versiones:** Git / GitHub

## 📁 Estructura del Proyecto
/pipeline-hurtos-bogota
  /notebooks/ -> Análisis exploratorio (Jupyter)
  /src/ -> Código ETL en .py
    extract.py
    transform.py
    load.py
  /dags/ -> DAG de Airflow
  /data/ -> Datos simulados
  requirements.txt

## 🚀 Cómo ejecutarlo
pip install -r requirements.txt
python src/extract.py

## 📊 Objetivo
Identificar patrones de hurto por localidad, hora y modalidad para proponer insights de seguridad.

Autor: Mario Gutierrez - Bogotá, Colombia
