# Databricks notebook source
import mlflow, mlflow.pyfunc

class SimpleModel(mlflow.pyfunc.PythonModel):
  def predict(self, context, model_input):
    return f'Hello {model_input}'

# COMMAND ----------

mlflow.pyfunc.save_model('/tmp/simple-model',python_model=SimpleModel(), input_example='World')

# COMMAND ----------

loaded_model = mlflow.pyfunc.load_model('/tmp/simple-model')
print(loaded_model.predict('World'))

# COMMAND ----------

with mlflow.start_run() as run:
  mlflow.pyfunc.log_model(artifact_path='models', python_model=SimpleModel(), registered_model_name='simple_model', input_example=['World'])

# COMMAND ----------


