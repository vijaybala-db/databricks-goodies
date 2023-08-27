# Databricks notebook source
# MAGIC %md
# MAGIC ## Web Application
# MAGIC
# MAGIC Create a flask application that allows the user to interact with the role-based advisor. 
# MAGIC
# MAGIC The front-end for this application, served at the `/` route is a HTML page that uses Bootstrap for styling. It consists of the following:
# MAGIC 1. A large text area that allows the user to type in their question
# MAGIC 2. Four buttons, one for each role, that let the user submit the question to the appropriate role-based advisor. They correspond to the following routes in the flask application:
# MAGIC   - `/ask/doctor`
# MAGIC   - `/ask/father`
# MAGIC   - `/ask/business_partner`
# MAGIC   - `/ask/career_coach`
# MAGIC 3. The back-end application should execute the `answer_as_role` function with the user question and role selected, and return the answer to the front end
# MAGIC 4. The front-end application should show the response to the user in the form of chat bubbles that are continuously appended at the bottom of the page

# COMMAND ----------

# MAGIC %sh
# MAGIC # Copy the Flask application and template to the driver directory
# MAGIC cp advisor.py /databricks/driver/
# MAGIC cp -r templates /databricks/driver/
# MAGIC # Install the systemd unit file
# MAGIC cp advisor.service /etc/systemd/system/
# MAGIC systemctl daemon-reload
# MAGIC systemctl enable advisor
# MAGIC systemctl restart advisor
# MAGIC systemctl status advisor

# COMMAND ----------

# MAGIC %md
# MAGIC ##### [Link](https://dbc-dp-1444828305810485.cloud.databricks.com/driver-proxy/o/1444828305810485/0822-051246-6h0nnn2l/8888)

# COMMAND ----------


