# chatbot.py

import google.generativeai as genai
from config import GEMINI_API_KEY

# Configure the API key
genai.configure(api_key=GEMINI_API_KEY)

# Load the Gemini Pro model with memory
model = genai.GenerativeModel("gemini-pro")
chat_session = model.start_chat(history=[])

def get_bot_response(user_input):
    try:
        response = chat_session.send_message(user_input)
        return response.text
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def get_full_history():
    return "\n".join(
        f"{item.role.title()}: {item.parts[0].text}" for item in chat_session.history
    )

def clear_history():
    global chat_session
    chat_session = model.start_chat(history=[])
