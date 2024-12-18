from flask import Flask, request, jsonify, send_from_directory
import os

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Route to serve the frontend
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

# Route to handle image uploads
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return jsonify({"success": "File uploaded successfully!", "filename": file.filename}), 200

if __name__ == '__main__':
    app.run(debug=True)
