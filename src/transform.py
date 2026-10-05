from pyspark.sql import SparkSession
import pandas as pd

def iniciar_spark():
    # En GCP esto sería Dataproc, aquí simulamos local
    spark = SparkSession.builder.appName("HurtosBogota").getOrCreate()
    return spark

def transformar_datos():
    print("Leyendo datos simulados...")
    df_pandas = pd.read_csv("data/hurtos_simulados.csv")

    # Lógica de transformación que te preguntan en entrevista
    print("\n--- Conteo por Localidad ---")
    print(df_pandas['localidad'].value_counts())
    
    print("\n--- Conteo por Modalidad ---")
    print(df_pandas['modalidad'].value_counts())

    # Simulación de lo que harías en PySpark
    # df_spark = spark.createDataFrame(df_pandas)
    # df_spark.groupBy("localidad").count().show()

    # Guardar dato limpio
    df_pandas.to_parquet("data/hurtos_limpios.parquet", index=False)
    print("\nDatos limpios guardados en data/hurtos_limpios.parquet")

if __name__ == "__main__":
    transformar_datos()
