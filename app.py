# app.py

from flask import Flask, render_template, request, redirect, url_for, jsonify
from chatbot import get_bot_response, get_full_history, clear_history
import os
from werkzeug.utils import secure_filename

# For file processing
try:
    import PyPDF2
except ImportError:
    PyPDF2 = None
try:
    import docx
except ImportError:
    docx = None
try:
    import pytesseract
    from PIL import Image
except ImportError:
    pytesseract = None
    Image = None

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    bot_response = ""
    user_input = ""

    if request.method == "POST":
        if 'ask' in request.form:
            user_input = request.form["query"]
            bot_response = get_bot_response(user_input)


        elif 'delete' in request.form:
            clear_history()
            bot_response = "🗑️ Chat history deleted permanently!"
            user_input = ""

        elif 'file' in request.files and request.files['file'].filename != "":
            file = request.files['file']
            try:
                text = extract_text_from_file(file)
                user_input = f"Summarize the uploaded file: {file.filename}"
                bot_response = summarize_text(text)
            except Exception as e:
                bot_response = f"⚠️ Error: {str(e)}"
                user_input = "File upload failed"

    chat_history = get_full_history()
    return render_template("index.html", query=user_input, response=bot_response, history=chat_history)

@app.route("/summarize", methods=["POST"])
def summarize_file():
    if 'file' not in request.files:
        return jsonify({'summary': 'No file uploaded.'}), 400
    file = request.files['file']
    filename = file.filename or ''
    if filename == '':
        return jsonify({'summary': 'No file selected.'}), 400
    filename = secure_filename(filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    ext = filename.lower().split('.')[-1]
    text = ''
    try:
        if ext == 'pdf' and PyPDF2:
            with open(filepath, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text = '\n'.join(page.extract_text() or '' for page in reader.pages)
        elif ext in ('doc', 'docx') and docx:
            doc = docx.Document(filepath)
            text = '\n'.join(para.text for para in doc.paragraphs)
        elif ext in ('png', 'jpg', 'jpeg', 'bmp') and pytesseract and Image:
            img = Image.open(filepath)
            text = pytesseract.image_to_string(img)
        else:
            return jsonify({'summary': 'Unsupported file type or missing dependencies.'}), 400
    except Exception as e:
        return jsonify({'summary': f'Error reading file: {str(e)}'}), 500
    if not text.strip():
        return jsonify({'summary': 'No text found in file.'}), 200
    try:
        from chatbot import get_bot_response
        summary = get_bot_response(f"Summarize this text in a concise way:\n{text[:4000]}")
    except Exception as e:
        summary = text[:1000] + ('...' if len(text) > 1000 else '')
    return jsonify({'summary': summary})

if __name__ == "__main__":
    app.run(debug=True)
