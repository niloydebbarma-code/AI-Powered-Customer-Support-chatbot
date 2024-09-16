from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Predefined utterances and responses
PREDEFINED_RESPONSES = {
    "what is your company about?": "Our company is dedicated to providing top-tier AI-powered customer support solutions to streamline business operations and enhance user experience.",
    "tell me about your services?": "We offer a range of services including AI-powered customer support, chatbot integration, and custom software solutions for businesses.",
    "can i know your business hours?": "Our business hours are Monday to Friday, 9:00 AM to 6:00 PM PST.",
    "where are you located?": "We are located in Los Angeles, California.",
    "how do i contact customer support?": "You can contact our customer support team via email at support@company.com or call us at +1 (800) 123-4567."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Get user input from the frontend
    user_message = request.json.get("message").lower()

    # Check if the message matches any predefined questions
    if user_message in PREDEFINED_RESPONSES:
        ai_response = PREDEFINED_RESPONSES[user_message]
    else:
        ai_response = "Sorry, I couldn't understand your question. Could you please rephrase?"

    return jsonify({"response": ai_response})

if __name__ == "__main__":
    app.run(debug=True, port=8080)
