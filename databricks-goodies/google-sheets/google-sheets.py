# Databricks notebook source
# MAGIC %md
# MAGIC # google-sheets
# MAGIC
# MAGIC Use a service account to connect to Google Sheets and retrieve a dataframe. 
# MAGIC
# MAGIC First, do the following:
# MAGIC 1. In your Google Cloud [Console](https://console.cloud.google.com), go to Credentials and create a service account
# MAGIC 2. Generate a key for the service account and download the credentials as a JSON file
# MAGIC 3. Store the credentials into Databricks secrets. Example CLI command is shown below:
# MAGIC ```
# MAGIC cat service_account.json| databricks secrets put-secret vbalasu partner-enablement
# MAGIC ```
# MAGIC 4. Share your spreadsheet with the service account (eg. partner-enablement@fe-dev-sandbox.iam.gserviceaccount.com)

# COMMAND ----------

# MAGIC %pip install gspread-pandas

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import os
home = os.path.expanduser('~')
try:
  os.mkdir(home + '/.config/gspread_pandas')
except FileExistsError:
  pass
credentials_filename = f'{home}/.config/gspread_pandas/google_secret.json'
with open(credentials_filename, 'w') as f:
  google_credentials = dbutils.secrets.get('vbalasu', 'partner-enablement')
  f.write(google_credentials)

# COMMAND ----------

from gspread_pandas import Spread
spread = Spread('1Jb29JaGXvOxSu0_MLK3XpvdnSd0SfnoWdcRD_bYQr0I')

# COMMAND ----------

df = spread.sheet_to_df(sheet='Vijay - Additional Resources', index=False)
df
