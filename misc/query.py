# coding: utf-8
from databricks import sql
import os
from sqlalchemy import create_engine
import pandas as pd

server_hostname = "adb-2548836972759138.18.azuredatabricks.net"
http_path = "/sql/1.0/warehouses/6d8c384eb165a20b"
access_token = os.environ.get('DATABRICKS_TOKEN')

engine = create_engine(
  url = f"databricks://token:{access_token}@{server_hostname}?" +
        f"http_path={http_path}&catalog=main&schema=data_df_metering"
)

df = pd.read_sql("""SELECT yyyymm, workspaceId, workspaceName, sku, sfdcAccountName, clusterId, 
netDbus, listPrice, ROUND(listPrice * netDbus, 2) dollars
FROM main.data_df_metering.workloads_cluster_agg
WHERE accountId IN (
    'e0e33ab0-450c-4297-8d4d-44982dee184d' --Deloitte
);""", engine)
print(df.to_json(orient='records'))
