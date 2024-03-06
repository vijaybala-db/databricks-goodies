# Databricks notebook source
# MAGIC %pip install --upgrade langchain databricks-genai-inference mlflow mlflow[databricks]
# MAGIC dbutils.library.restartPython()

# COMMAND ----------

def mermaid(definition):
  import IPython
  return IPython.display.HTML(f"""<pre class="mermaid">{definition}</pre>
    <script src="https://cdn.jsdelivr.net/npm/mermaid@10.8.0/dist/mermaid.min.js"></script>""")

# COMMAND ----------

mermaid("""graph LR;
            user_input --> prompt --> chat_model --> output_parser --> lambda_function""")

# COMMAND ----------

# https://python.langchain.com/docs/integrations/llms/databricks
# https://python.langchain.com/docs/modules/model_io/prompts/quick_start
# https://python.langchain.com/docs/expression_language/get_started
# https://docs.databricks.com/en/machine-learning/model-serving/score-foundation-models.html#language-LangChain
from langchain_community.chat_models.databricks import ChatDatabricks
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.output_parsers import StrOutputParser
store = {}
prompt = ChatPromptTemplate.from_messages([
  ('system', 'You are a very patient and friendly teacher who likes to explain things step by step'),
  MessagesPlaceholder(variable_name='history'),
  ('human', '{user_input}')
])
chat_model = ChatDatabricks(endpoint="databricks-mixtral-8x7b-instruct", max_tokens=500)
output_parser = StrOutputParser()

# COMMAND ----------

runnable = prompt | chat_model | output_parser

# COMMAND ----------

def get_session_history(session_id: str) -> BaseChatMessageHistory:
  if session_id not in store:
    store[session_id] = ChatMessageHistory()
  return store[session_id]

with_message_history = RunnableWithMessageHistory(runnable, get_session_history, input_messages_key='user_input', 
                                                  history_messages_key='history')                                                

# COMMAND ----------

with_message_history.invoke(
    {"user_input": "What tree fits in your hand?"},
    config={"configurable": {"session_id": "abcxyz"}},
)

# COMMAND ----------

with_message_history.invoke(
    {"user_input": "What conditions?"},
    config={"configurable": {"session_id": "abcxyz"}},
)

# COMMAND ----------

with_message_history.get_session_history('abcxyz')

# COMMAND ----------


