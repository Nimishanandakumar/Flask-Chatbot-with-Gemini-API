import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Set your API key here
API_KEY = "Your API KEy"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

app = Flask(__name__)

# Define the chatbot function
def chatbot_response(user_input):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(user_input)
    return response.text

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for handling chatbot responses
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = chatbot_response(user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
                            