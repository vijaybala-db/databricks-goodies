# Databricks notebook source
import sqlite3, pandas as pd
conn = sqlite3.connect('/Volumes/vijay_balasubramaniam/default/files/northwind.db')
cur = conn.cursor()
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [t[0] for t in cur.fetchall()]
for table in tables:
  try:
    df = pd.read_sql(f'SELECT * FROM {table};', conn)
    spark.createDataFrame(df).write.format('delta').mode('overwrite').saveAsTable(f'vijay_balasubramaniam.default.{table}')
  except:
    pass
conn.close()

# COMMAND ----------

conn = sqlite3.connect('/Volumes/vijay_balasubramaniam/default/files/northwind.db')
conn.close()
tables

# COMMAND ----------

# Load the sqlite3 file into a spark dataframe
spark_df = spark.read.format('jdbc').\
    option('url', 'jdbc:sqlite:/dbfs/tmp/northwind.db').\
    option('dbtable', 'Customers').\
    option('driver', 'org.sqlite.JDBC').\
    load()

# COMMAND ----------

display(spark_df)

# COMMAND ----------


