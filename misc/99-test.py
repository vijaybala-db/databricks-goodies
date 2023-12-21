# Databricks notebook source
import sys
sys.path.append('/Workspace/Repos/vijay.balasubramaniam@databricks.com/databricks-goodies/role-based-advisor')
from advisor import RoleBasedAdvisor

# COMMAND ----------

llamav2_advisor = RoleBasedAdvisor(language_model='llamav2')
llamav2_answer = llamav2_advisor.answer_as_role('What should I do with my life?', 'doctor')
print(llamav2_answer)

# COMMAND ----------

openai_advisor = RoleBasedAdvisor(language_model='openai')
openai_answer = openai_advisor.answer_as_role('What should I do with my life', 'doctor')
print(openai_answer)

# COMMAND ----------

from dbruntime.databricks_repl_context import get_context
ctx = get_context()

port = "7777"
driver_proxy_api = f"https://{ctx.browserHostName}/driver-proxy-api/o/0/{ctx.clusterId}/{port}"

print(f"""
driver_proxy_api = '{driver_proxy_api}'
cluster_id = '{ctx.clusterId}'
port = {port}
""")

# COMMAND ----------

vars(ctx)

# COMMAND ----------

import socket
socket.gethostname()


# COMMAND ----------

# MAGIC %pip install streamlit

# COMMAND ----------

import streamlit as st
st.title('Hello world')

# COMMAND ----------

!streamlit run /databricks/python_shell/scripts/db_ipykernel_launcher.py

# COMMAND ----------

!curl http://localhost:7777

# COMMAND ----------

# MAGIC %md
# MAGIC <img src="https://raw.githubusercontent.com/vbalasu/databricks-goodies/main/media/businessman-shaking-hands-svgrepo-com.svg" width="300px" />

# COMMAND ----------


