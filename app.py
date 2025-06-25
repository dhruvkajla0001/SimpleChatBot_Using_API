from flask import Flask, render_template, request, session
from chatbot import get_bot_response, get_full_history, clear_history
from utils import extract_text_from_file, summarize_text
import os

app = Flask(__name__)
app.secret_key = "super_secret_key"  # Required for session handling

@app.route("/", methods=["GET", "POST"])
def index():
    bot_response = ""
    user_input = ""

    if request.method == "POST":
        if 'ask' in request.form:
            user_input = request.form["query"]
            bot_response = get_bot_response(user_input)

        elif 'clear' in request.form:
            clear_history()
            bot_response = "🧹 Chat history cleared!"
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

if __name__ == "__main__":
    app.run(debug=True)
