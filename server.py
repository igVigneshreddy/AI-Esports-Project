from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
API_KEY = "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"  # <<< Replace this!

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    payload = {
        "inputs": user_message,
        "parameters": {
            "temperature": 0.7,
            "max_new_tokens": 300
        }
    }
    
    response = requests.post(API_URL, headers=headers, json=payload)
    result = response.json()

    if isinstance(result, list):
        reply = result[0]['generated_text']
    else:
        reply = "Sorry, something went wrong!"

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
