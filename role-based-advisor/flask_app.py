from flask import Flask, render_template, request, jsonify
import os
from advisor import RoleBasedAdvisor

# Create advisor objects for OpenAI and Llama V2
openai_advisor = RoleBasedAdvisor(language_model='openai')
if 'DATABRICKS_RUNTIME_VERSION' in os.environ:
    llamav2_advisor = RoleBasedAdvisor(language_model='llamav2', 
                                    config_file_path='/tmp/llamav2_config.json')

app = Flask("role-based-advisor")

# Simulated function to provide answers based on roles
def answer_as_role(question, role):
    # answer = openai_advisor.answer_as_role(question, role, verbose=True)
    answers = {
        "doctor": "I'm a doctor and here's my advice...",
        "father": "As a father, I suggest...",
        "business_partner": "From a business partner perspective...",
        "career_coach": "As a career coach, I recommend..."
    }
    # return answer
    return answers[role]

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/hello')
def hello():
  return 'hello'

@app.route('/ask/<role>', methods=['POST'])
def ask(role):
    data = request.json
    print(data)
    answer = answer_as_role(data['question'], data['role'])
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8888", debug=True, use_reloader=False)