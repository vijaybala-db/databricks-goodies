# Databricks notebook source
# MAGIC %md
# MAGIC ## Role-based Advisor
# MAGIC
# MAGIC This notebook demonstrates how to build a role-based advisor using a large language model. The AI can play a role such as the following:
# MAGIC
# MAGIC - Doctor
# MAGIC - Father
# MAGIC - Business partner
# MAGIC - Career coach
# MAGIC
# MAGIC The user can ask a question such as the following:
# MAGIC ```
# MAGIC I want to live a life that maximizes happiness and creates a positive impact on the world. 
# MAGIC What are the top 5 things I should do in the next week towards these goals?
# MAGIC ```
# MAGIC
# MAGIC and receive answers from each role's perspective.

# COMMAND ----------

import openai, os
from langchain.llms import Databricks, OpenAI

# COMMAND ----------

def switch_to_language_model(language_model):
  if language_model == 'openai':
    os.environ['OPENAI_API_KEY'] = dbutils.secrets.get('vbalasu', 'openai-databricks')
    llm = OpenAI(temperature=0.0, max_tokens=500)
    return llm
  elif language_model == 'llamav2':
    llm = Databricks(cluster_driver_port=7777, cluster_id='0818-171600-mjlzuq5m',
                  model_kwargs={'temperature':0.0, 'max_new_tokens':500})
    return llm
  else:
    print('Unknown language model')
    return False

# COMMAND ----------

template_string = """{role_name} \
Respond to the user question that is delimited in triple backticks \
with thoughtful and concise instructions that the user can easily implement in their \
day to day life.
user_question: ```{user_question}```
"""

# COMMAND ----------

role_doctor = """You are a doctor (primary care physician) with 25 years of experience practicing in California. You emphasize the importance of a healthy lifestyle that includes nutritious food and vigorous exercise."""

role_father = """You are the user's father and cares deeply about their well being. You emphasize the importance of working hard and getting a good education."""

role_business_partner = """You are the user's business partner. You share a mutual interest in the success of your company. You emphasize actions that will maximize the long term viability and profitability of the company and achieving its mission."""

role_career_coach = """You are the user's manager at work. You see great potential in the user to progress in their career. You emphasize actions that maximize the user's chances for a promotion and continue their trajectory to become a senior executive."""

user_question = "I want to live a life that maximizes happiness and creates a positive impact on the world. What are the top 5 things I should do in the next week towards these goals?"

# COMMAND ----------

from langchain.prompts import ChatPromptTemplate
def answer_as_role(user_question, role, verbose=False):
  prompt_template = ChatPromptTemplate.from_template(template_string)
  prompt = prompt_template.format_prompt(role_name=role, user_question=user_question)
  question = prompt.messages[0].content
  if verbose:
    print('/*\n', f'LANGUAGE MODEL: {language_model}\n\n', question, '*/\n\n')
  return llm(question)

# COMMAND ----------

# MAGIC %md
# MAGIC ### OpenAI

# COMMAND ----------

language_model = 'openai'
llm = switch_to_language_model(language_model)

# COMMAND ----------

answer = answer_as_role(user_question, role_doctor, verbose=True)
print(answer)

# COMMAND ----------

answer = answer_as_role(user_question, role_father, verbose=True)
print(answer)

# COMMAND ----------

answer = answer_as_role(user_question, role_business_partner, verbose=True)
print(answer)

# COMMAND ----------

answer = answer_as_role(user_question, role_career_coach, verbose=True)
print(answer)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Llama V2

# COMMAND ----------

language_model = 'llamav2'
llm = switch_to_language_model(language_model)

# COMMAND ----------

answer = answer_as_role(user_question, role_doctor, verbose=True)
print(answer)

# COMMAND ----------

answer = answer_as_role(user_question, role_father, verbose=True)
print(answer)

# COMMAND ----------

answer = answer_as_role(user_question, role_business_partner, verbose=True)
print(answer)

# COMMAND ----------

answer = answer_as_role(user_question, role_career_coach, verbose=True)
print(answer)
