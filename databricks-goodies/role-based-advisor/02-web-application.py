# Databricks notebook source
# MAGIC %md
# MAGIC ## Web Application
# MAGIC
# MAGIC Create a Streamlit application that allows the user to interact with the role-based advisor. 
# MAGIC
# MAGIC The front-end for this application consists of the following:
# MAGIC 1. A large text area that allows the user to type in their question
# MAGIC 2. Radio buttons, one for each role, that let the user submit the question to the appropriate role-based advisor. They correspond to the following roles:
# MAGIC   - Doctor
# MAGIC   - Father
# MAGIC   - Business Partner
# MAGIC   - Career Coach
# MAGIC 3. The back-end application should execute the `answer_as_role` function with the user question and role selected, and return the answer to the front end
# MAGIC 4. The front-end application should show the response to the user

# COMMAND ----------

# MAGIC %pip install streamlit

# COMMAND ----------

# Get the front part of the URL by launching a web terminal
# Then set a different port
port = '8888'
url = f'https://dbc-dp-1444828305810485.cloud.databricks.com/driver-proxy/o/1444828305810485/0822-051246-6h0nnn2l/{port}/'
displayHTML(f'<a href="{url}">{url}</a>')

# COMMAND ----------

print('Launch the app using the link above')
!streamlit run app.py --server.port {port} >/dev/null
