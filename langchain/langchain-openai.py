# Databricks notebook source
import os
os.environ["OPENAI_API_KEY"] = dbutils.secrets.get(scope='vbalasu', key='openai-databricks')

# COMMAND ----------

import openai
def get_completion(prompt, model="gpt-3.5-turbo"):
  messages = [{"role": "user", "content": prompt}]
  response = openai.ChatCompletion.create(
    model=model,
    messages=messages,
    temperature=0
  )
  return response.choices[0].message['content']

# COMMAND ----------

get_completion('What is 1+1')

# COMMAND ----------

from langchain.chat_models import ChatOpenAI
chat = ChatOpenAI(temperature=0.0)
chat

# COMMAND ----------

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

# COMMAND ----------

from langchain.prompts import ChatPromptTemplate
prompt_template = ChatPromptTemplate.from_template(template_string)
prompt_template

# COMMAND ----------

prompt_template.messages[0].prompt.input_variables

# COMMAND ----------

customer_messages = prompt_template.format_messages(style='American English in a calm and respectful tone', text='Arrr, what a fantabulous jewel matey!')

# COMMAND ----------

customer_messages[0]

# COMMAND ----------

customer_response = chat(customer_messages)

# COMMAND ----------

customer_response.content

# COMMAND ----------

{
  "gift": False,
  "delivery_days": 5,
  "price_value": "pretty affordable!"
}.get('gift')

# COMMAND ----------


