# Databricks notebook source
# MAGIC %md
# MAGIC # Capture location data and ingest it into the Lakehouse

# COMMAND ----------

!aws s3 ls s3://databricks-partners/

# COMMAND ----------

# MAGIC %pip install geocoder

# COMMAND ----------

import datetime, json
import geocoder
g = geocoder.ip('me')
data = {'when': datetime.datetime.utcnow().isoformat(), 'latitude': g.latlng[0], 'longitude': g.latlng[1]}
json.dumps(data)

# COMMAND ----------

with open('/dbfs/tmp/location.json', 'w') as f:
  f.write(json.dumps(data))

# COMMAND ----------

!aws s3 cp /dbfs/tmp/location.json s3://databricks-partners/location/location.json

# COMMAND ----------

# MAGIC %sql
# MAGIC --DROP TABLE vijay_b.location;
# MAGIC CREATE TABLE vijay_b.location USING JSON LOCATION '/tmp/location.json';

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM vijay_b.location;

# COMMAND ----------

!ls -l /dbfs/tmp/*.csv

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM csv.`/tmp/customer_churn.csv`

# COMMAND ----------


