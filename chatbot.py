# chatbot.py

import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

# Memory to store chat
chat_history = [
    {"role": "system", "content": "You are a helpful and smart assistant."}
]

def get_bot_response(user_input):
    try:
        chat_history.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            messages=chat_history
        )
        answer = response.choices[0].message["content"]
        chat_history.append({"role": "assistant", "content": answer})
        return answer
    except Exception as e:
        return f"⚠️ Error: {str(e)}"

def get_full_history():
    return "\n".join(
        f"{m['role'].capitalize()}: {m['content']}"
        for m in chat_history
        if m["role"] != "system"
    )

def clear_history():
    global chat_history
    chat_history = [
        {"role": "system", "content": "You are a helpful and smart assistant."}
    ]
