# Databricks notebook source
# MAGIC %pip install gspread-pandas

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import gspread_pandas
spread = gspread_pandas.spread.Spread('1Nxj_hWUKfa4UWlOvXZaI7jgV_o-6e5ShRfYXbhiRHN4')

# COMMAND ----------

# MAGIC %md
# MAGIC The first time you run the above command, it prompts you to complete the OAuth2 flow
# MAGIC The redirect back from Google to Databricks fails
# MAGIC However, you can complete the OAuth2 flow on your local machine and copy the resulting credentials to this file on your Databricks cluster:
# MAGIC
# MAGIC ```~/.config/gspread_pandas/creds/default```
# MAGIC
# MAGIC

# COMMAND ----------

df = spread.sheet_to_df(sheet='genai_recent_metering', index=False)
df

# COMMAND ----------


