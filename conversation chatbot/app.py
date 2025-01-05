import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai

# Set your API key here
API_KEY = "Your API Key"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

app = Flask(__name__)

# Initialize conversation history
conversation_history = []

# Define the chatbot function
def chatbot_response(user_input):
    # Add the user input to the conversation history
    conversation_history.append(f":User  {user_input}")
    
    # Create a prompt from the conversation history
    prompt = "\n".join(conversation_history) + "\nBot:"
    
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    
    # Get the bot's response
    bot_reply = response.text.strip()
    
    # Add the bot's response to the conversation history
    conversation_history.append(f"Bot: {bot_reply}")
    
    return bot_reply

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html', conversation=conversation_history)

# Route for handling chatbot responses
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('input')
    response = chatbot_response(user_input)
    return jsonify({'response': response, 'conversation': conversation_history})

if __name__ == '__main__':
    app.run(debug=True)