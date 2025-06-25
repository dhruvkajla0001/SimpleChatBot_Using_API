# app.py

from flask import Flask, render_template, request, redirect, url_for
from chatbot import get_bot_response, get_full_history, clear_history

app = Flask(__name__)

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

    chat_history = get_full_history()
    return render_template("index.html", query=user_input, response=bot_response, history=chat_history)

if __name__ == "__main__":
    app.run(debug=True)
