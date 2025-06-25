# chatbot.py

import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure your Gemini API key
genai.configure(api_key=GEMINI_API_KEY)

# Correct model name with full path
model = genai.GenerativeModel("models/gemini-2.0-flash")


# Chat session with memory
chat = model.start_chat(history=[])

def get_bot_response(user_input):
    try:
        response = chat.send_message(user_input)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def get_full_history():
    return "\n".join(
        f"{item.role.title()}: {item.parts[0].text}" for item in chat.history
    )

def clear_history():
    global chat
    chat = model.start_chat(history=[])
