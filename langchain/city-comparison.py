# Databricks notebook source
# MAGIC %md
# MAGIC # City Comparison

# COMMAND ----------

# MAGIC %pip install --upgrade langchain mlflow

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

from langchain_community.chat_models.databricks import ChatDatabricks
chat = ChatDatabricks(endpoint='databricks-llama-2-70b-chat', extra_params={'temperature': 0.0})

# COMMAND ----------

# MAGIC %md
# MAGIC ### Identify Candidate Cities

# COMMAND ----------

response = chat.invoke('Please list the names of the top 20 cities in the USA based on economic opportunity. Your response should only the city and state names and nothing else. The output should be a properly formatted JSON document that consists of an array of objects with keys "city" and "state". Do not output anything other than the JSON array')
print(response.content)

# COMMAND ----------

import json
import pandas as pd
df = pd.DataFrame(json.loads(response.content)['cities'])
df

# COMMAND ----------

city = 'Boston'
state = 'Massachusetts'
response = chat.invoke(f'What is the average summer high temperature in {city}, {state}? Your response should only the temperature in farenheit and nothing else.')
print(response.content)

# COMMAND ----------

# MAGIC %md
# MAGIC Now that our prompt is working, let's wrap it into a Langchain chain

# COMMAND ----------

# MAGIC %md
# MAGIC #### Average Summer High Temperatures

# COMMAND ----------

from langchain_core.prompts import ChatPromptTemplate
summer_high_prompt = ChatPromptTemplate.from_template('What is the average summer high temperature in {city}, {state}? Your response should only the temperature in farenheit and nothing else.')
summer_high_prompt

# COMMAND ----------

from langchain.chains import LLMChain
summer_high_chain = LLMChain(llm=chat, prompt=summer_high_prompt, verbose=True)
summer_high_chain

# COMMAND ----------

response = summer_high_chain.invoke({'city': 'Denver', 'state': 'Colorado'})
response

# COMMAND ----------

def parse_summer_high_temperature(row):
  print(row)
  response = summer_high_chain.invoke({'city': row.city, 'state': row.state})
  return response['text'].replace('\n', '').replace('°F', '')
df['avg_summer_high_temp'] = df.apply(parse_summer_high_temperature, axis=1)
df

# COMMAND ----------

# MAGIC %md
# MAGIC #### Average Winter Low Temperatures

# COMMAND ----------

from langchain_core.prompts import ChatPromptTemplate
winter_low_prompt = ChatPromptTemplate.from_template('What is the average winter low temperature in {city}, {state}? Your response should only the temperature in farenheit and nothing else.')
winter_low_prompt

# COMMAND ----------

from langchain.chains import LLMChain
winter_low_chain = LLMChain(llm=chat, prompt=winter_low_prompt, verbose=True)
winter_low_chain

# COMMAND ----------

def parse_winter_low_temperature(row):
  print(row)
  response = winter_low_chain.invoke({'city': row.city, 'state': row.state})
  return response['text'].replace('\n', '').replace('°F', '')
df['avg_winter_low_temp'] = df.apply(parse_winter_low_temperature, axis=1)
df

# COMMAND ----------

df.to_json()

# COMMAND ----------

# MAGIC %md
# MAGIC Generated the data visualization code using ChatGPT
# MAGIC
# MAGIC https://chat.openai.com/share/f29688fe-8fce-44a6-bf8a-5deab7b058f9

# COMMAND ----------

import pandas as pd
import plotly.express as px

# [Insert the DataFrame creation code here]

# Converting temperature columns to numeric
df['avg_summer_high_temp'] = pd.to_numeric(df['avg_summer_high_temp'])
df['avg_winter_low_temp'] = pd.to_numeric(df['avg_winter_low_temp'])

# Creating scatter plot using plotly express with city names displayed
fig = px.scatter(df, x='avg_summer_high_temp', y='avg_winter_low_temp', 
                 text='city',  # This line adds city names next to each point
                 hover_name='city', 
                 hover_data=['avg_summer_high_temp', 'avg_winter_low_temp'],
                 title='Average Summer High Temp vs. Average Winter Low Temp',
                 labels={'avg_summer_high_temp': 'Average Summer High Temperature (°F)', 
                         'avg_winter_low_temp': 'Average Winter Low Temperature (°F)'})

# Adjusting text position for clarity
fig.update_traces(textposition='middle right')
fig.update_layout(showlegend=False)

# Setting the height of the plot (e.g., 600 pixels)
fig.update_layout(height=600)

fig.show()


# COMMAND ----------


