# Databricks notebook source
# MAGIC %pip install PyPDF2 requests

# COMMAND ----------

import mlflow, mlflow.pyfunc

class PdfProcessor(mlflow.pyfunc.PythonModel):
  def fetch_pdf(self, url):
    import requests
    response = requests.get(url)
    return response.content
  def predict(self, context, model_input):
    print(model_input)
    url = model_input['url'][0]
    content_bytes = self.fetch_pdf(url)
    return str(content_bytes)

# COMMAND ----------

import pandas as pd
df = pd.DataFrame({"url":["https://arxiv.org/pdf/2310.12155.pdf"]})
df

# COMMAND ----------

model = PdfProcessor()
model.predict(None, df)

# COMMAND ----------

with mlflow.start_run() as run:
  mlflow.pyfunc.log_model(artifact_path='models', python_model=PdfProcessor(), registered_model_name='pdf_processor', input_example='https://arxiv.org/pdf/2310.12155.pdf', pip_requirements=['requests'])

print('Run ID: ', run.info.run_id)

# COMMAND ----------


