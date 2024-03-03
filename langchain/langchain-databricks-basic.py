# Databricks notebook source
# MAGIC %pip install --upgrade langchain databricks-genai-inference mlflow mlflow[databricks]
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

# https://python.langchain.com/docs/integrations/llms/databricks
# https://python.langchain.com/docs/modules/model_io/prompts/quick_start
# https://python.langchain.com/docs/expression_language/get_started
# https://docs.databricks.com/en/machine-learning/model-serving/score-foundation-models.html#language-LangChain
from langchain_community.chat_models.databricks import ChatDatabricks
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
prompt = ChatPromptTemplate.from_messages([
  ('system', 'You are a very patient and friendly teacher who likes to explain things step by step'),
   ('human', '{user_input}')
])
chat_model = ChatDatabricks(endpoint="databricks-mixtral-8x7b-instruct", max_tokens=500)
output_parser = StrOutputParser()
chain = ({'user_input': RunnablePassthrough()} | prompt | chat_model | output_parser)
print(chain.invoke('How to write a blog post?'))

# COMMAND ----------

# Invoke arbitrary function
from langchain_core.runnables import RunnableLambda
newchain = (chain | RunnableLambda(lambda x:x.upper()))
newchain.invoke('What tree fits in your hand?')

# COMMAND ----------


