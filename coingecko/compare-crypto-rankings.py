# Databricks notebook source
# MAGIC %md
# MAGIC # compare-crypto-rankings
# MAGIC
# MAGIC Compare today's Coingecko
# MAGIC  rankings Vs 6 months ago

# COMMAND ----------

import datetime, dateutil
today = datetime.date.today()
before_6_mo = today - dateutil.relativedelta.relativedelta(months=6)
before_6_mo

# COMMAND ----------

formatted_prior = before_6_mo.strftime('%d-%m-%Y')
formatted_prior

# COMMAND ----------

import requests
response = requests.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&per_page=250&order=market_cap_desc&page=1')
data = response.json()
data

# COMMAND ----------

import pandas as pd
pd.DataFrame(data)

# COMMAND ----------

data[0]['id']

# COMMAND ----------

def get_history(id, as_of_date):
  url = f'https://api.coingecko.com/api/v3/coins/{id}/history?date={as_of_date}&localization=false'
  response = requests.get(url)
  history = response.json()
  import json
  with open(f'/tmp/{id}_{as_of_date}.json', 'w') as f:
    json.dump(history, f)
  return history

# COMMAND ----------

# Loop through and save history for each coin
# 200ms delay is included to respect API rate limit
import time
all_history = []
for ctr, d in enumerate(data):
  id = d['id']
  try:
    print(ctr, id, d['current_price'])
  except:
    print('ERROR', d)
  history = get_history(id, formatted_prior)
  all_history.append(history)
  time.sleep(6)

# COMMAND ----------

!ls -larth /tmp/

# COMMAND ----------

all_history[4]

# COMMAND ----------

from IPython.display import display, clear_output
import time
import ipywidgets as widgets

# Create a text widget
text_widget = widgets.Textarea(
    value='',
    placeholder='Values will appear here',
    description='Latest Values:',
    disabled=False,
    layout={'width': '400px', 'height': '100px'}
)

# Display the text widget
display(text_widget)

# Continuous update loop
for i in range(1, 101):  # Adjust the range as needed
    # Prepare the text with the last three values
    new_text = ', '.join(str(j) for j in range(max(1, i-2), i+1))

    # Update the text widget
    text_widget.value = new_text

    # Wait for a second
    time.sleep(1)


# COMMAND ----------

import plotly.graph_objs as go
from IPython.display import display, clear_output
import time
import numpy as np

# Function to update the plot
def update_plot(n):
    x = np.arange(n)
    y = x ** 2
    fig = go.Figure(data=[go.Scatter(x=x, y=y)])
    fig.show()

# Continuous update loop
for i in range(1, 10):  # Adjust the range as needed
    clear_output(wait=True)
    update_plot(i)
    time.sleep(1)  # Update every second


# COMMAND ----------


