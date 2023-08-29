from flask import Flask, render_template, request, jsonify
from advisor import RoleBasedAdvisor

# Create advisor objects for OpenAI and Llama V2
openai_advisor = RoleBasedAdvisor(language_model='openai')
llamav2_advisor = RoleBasedAdvisor(language_model='llamav2')

app = Flask("role-based-advisor")

# Simulated function to provide answers based on roles
def answer_as_role(question, role):
    # You can implement your logic here to return appropriate answers for each role
    answers = {
        "doctor": "I'm a doctor and here's my advice...",
        "father": "As a father, I suggest...",
        "business_partner": "From a business partner perspective...",
        "career_coach": "As a career coach, I recommend..."
    }
    return answers.get(role, "Invalid role")

@app.route('/')
def index():
    return render_template('index.html')
  
@app.route('/hello')
def hello():
  return 'hello'

@app.route('/ask/<role>', methods=['POST'])
def ask(role):
    return request.json
    #question = request.form['question']
    #answer = answer_as_role(question, role)
    #return jsonify({"role", role})
    # return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8888", debug=True, use_reloader=False)