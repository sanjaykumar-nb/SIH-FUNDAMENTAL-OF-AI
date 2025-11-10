from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from backend.models.chat_model import answer_question
from backend.utils.bad_language_filter import filter_bad_language
from backend.utils.auth_utils import send_otp, verify_otp
from backend.utils.document_utils import process_document

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = 'docs/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# In-memory for demo
otp_store = {}

@app.route('/')
def root():
    return send_from_directory('../frontend', 'index.html')

@app.route('/auth/login', methods=['POST'])
def login():
    data = request.json
    email = data['email']
    otp = send_otp(email)
    otp_store[email] = otp
    return jsonify({"message": "OTP sent"})

@app.route('/auth/verify', methods=['POST'])
def verify():
    data = request.json
    email = data['email']
    otp = data['otp']
    if otp_store.get(email) == otp:
        del otp_store[email]
        return jsonify({"message": "Verified", "token": "dummy_token"})
    return jsonify({"error": "Invalid OTP"}), 400

@app.route('/chat/message', methods=['POST'])
def chat_message():
    data = request.json
    message = data['message']
    filtered = filter_bad_language(message)
    if filtered != message:
        return jsonify({"response": "Please refrain from using inappropriate language."})
    response = answer_question(filtered)
    return jsonify({"response": response})

@app.route('/document/upload', methods=['POST'])
def upload_document():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if not file.filename.endswith(('.pdf', '.docx', '.txt')):
        return jsonify({"error": "Invalid file type"}), 400
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)
    result = process_document(file_path)
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
