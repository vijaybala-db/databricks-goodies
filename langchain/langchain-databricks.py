# Databricks notebook source
# MAGIC %pip install --upgrade mlflow mlflow[databricks] langchain

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import os
os.environ["DATABRICKS_HOST"] = "https://e2-demo-west.cloud.databricks.com" # set to your server URI
os.environ["DATABRICKS_TOKEN"] = dbutils.secrets.get('vbalasu', 'e2-demo-west-token')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Use Without Langchain

# COMMAND ----------

#!pip install mlflow mlflow[databricks]
import mlflow.deployments
client = mlflow.deployments.get_deploy_client('databricks')
inputs = {
  "messages": [
    {
      "role": "user",
      "content": "Hello!"
    },
    {
      "role": "assistant",
      "content": "Hello! How can I assist you today?"
    },
    {
      "role": "user",
      "content": "What is Databricks?"
    }
  ],
  "max_tokens": 128
}
response = client.predict(endpoint="databricks-llama-2-70b-chat", inputs=inputs)
response

# COMMAND ----------

# MAGIC %md
# MAGIC ### With Langchain

# COMMAND ----------

# https://python.langchain.com/docs/integrations/llms/databricks
from langchain_community.chat_models import ChatDatabricks
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatDatabricks(target_uri="databricks", endpoint='databricks-llama-2-70b-chat', temperature=0.0)
chat.invoke([SystemMessage(content='You are a helpful assistant that offers help about computers'), 
             HumanMessage(content="hello")])

# COMMAND ----------


