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

from langchain.globals import set_verbose, set_debug
set_verbose(True)

# COMMAND ----------

# https://python.langchain.com/docs/integrations/llms/databricks
from langchain_community.chat_models import ChatDatabricks
from langchain_core.messages import HumanMessage, SystemMessage

chat = ChatDatabricks(target_uri="databricks", endpoint='databricks-llama-2-70b-chat', temperature=0.0)
chat.invoke([SystemMessage(content='You are a helpful assistant that offers help about computers'), 
             HumanMessage(content="hello")])

# COMMAND ----------

# Non Chat Model
from langchain_community.llms.databricks import Databricks
llm = Databricks(endpoint_name='databricks-mpt-30b-instruct')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Nutritional Advisor

# COMMAND ----------

# https://python.langchain.com/docs/modules/model_io/prompts/quick_start#chatprompttemplate
from langchain_core.prompts import ChatPromptTemplate
chat_template = ChatPromptTemplate.from_messages([
  ('system', 'You are a helpful AI bot. You offer insights about the nutritional value of various fruits'),
  ('human', 'Hi, how are you?'),
  ('ai', 'I am doing well, thanks!'),
  ('human', '{user_input}')
])
chat_template

# COMMAND ----------

messages = chat_template.format_messages(user_input='Tell me about avocados')
messages

# COMMAND ----------

response = chat.invoke(messages)
print(response.content)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Output Parser
# MAGIC https://python.langchain.com/docs/modules/model_io/output_parsers/types/structured
# MAGIC https://python.langchain.com/docs/modules/model_io/output_parsers/types/json

# COMMAND ----------

# from langchain.output_parsers import ResponseSchema, StructuredOutputParser
# calories_schema = ResponseSchema(name='calories', description='Total calories')
# fat_schema = ResponseSchema(name='fat', description='Total fat in grams')
# carbohydrates_schema = ResponseSchema(name='carbohydrates', description='Total carbohydrates in grams')
# sodium_schema = ResponseSchema(name='sodium', description='Total sodium in milligrams')
# response_schemas = [calories_schema, fat_schema, carbohydrates_schema, sodium_schema]

# COMMAND ----------

# output_parser = StructuredOutputParser.from_response_schemas(response_schemas)
# format_instructions = output_parser.get_format_instructions()
# format_instructions

# COMMAND ----------

from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
class NutritionFacts(BaseModel):
  calories: float = Field(description='Total calories')
  fat: float = Field(description='Total fat in grams')
  carbohydrates: float = Field(description='Total carbohydrates in grams')
  sodium: float = Field(description='Total sodium in milligrams')
parser = JsonOutputParser(pydantic_object=NutritionFacts)
parser.get_format_instructions()

# COMMAND ----------

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate(template="Provide information about the nutritional value of {user_input}", 
                        input_variables=['user_input'], partial_variables={'format_instructions': parser.get_format_instructions()})
prompt

# COMMAND ----------

import os
os.environ["OPENAI_API_KEY"] = dbutils.secrets.get(scope='vbalasu', key='openai-databricks')
from langchain.chat_models import ChatOpenAI
model = ChatOpenAI(temperature=0.0)

# COMMAND ----------

#model = ChatDatabricks(target_uri="databricks", endpoint='databricks-llama-2-70b-chat', temperature=0.0)

# COMMAND ----------

chain = prompt | model
chain.invoke({'user_input': 'Tell me about avocados'})

# COMMAND ----------

chain

# COMMAND ----------


