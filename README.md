# ProBot - Your Professional Assistant

ProBot is a modern, stylish chatbot web app built with Flask and Google Gemini API. It provides instant, reliable answers and professional insights, with a beautiful black/yellow UI, chat history, file upload, and voice input.

---

## ✨ Features
- **Conversational AI** powered by Google Gemini (Gemini 2.0 Flash)
- **Modern UI**: Black, white, and yellow theme with smooth transitions
- **Chat History**: View and clear your conversation history
- **File Upload**: Upload `.txt`, `.pdf`, or `.docx` files for instant summarization
- **Voice Input**: Ask questions using your microphone (Chrome/Edge recommended)
- **Responsive Layout**: Works on desktop and mobile
- **Custom Scrollbars**: Only in chat output and history for a clean look

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone <repo-url>
cd SimpleChatBot_Using_API
```

### 2. Install dependencies
Make sure you have Python 3.8+ and pip installed.
```bash
pip install flask google-generativeai PyPDF2 python-docx
```

### 3. Configure your Gemini API key
Edit `config.py` and set your Gemini API key:
```python
GEMINI_API_KEY = "your-gemini-api-key-here"
```

### 4. Run the app
```bash
python app.py
```
Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🖥️ UI Highlights
- **Left:** Chat history with a static "Clear Chat" button and custom scrollbar
- **Right:** Main chat area with:
  - Input box
  - Voice input button
  - Attractive "Choose File" button for uploads
  - Send and Clear buttons
  - Chat output with yellow/black scrollable area
- **Modern transitions** and responsive design

---

## 📄 Supported File Types
- `.txt` (plain text)
- `.pdf` (PDF documents)
- `.docx` (Word documents)

---

## 🗣️ Voice Input
- Works best in Chrome or Edge (uses Web Speech API)

---

## 🖼️ Screenshots
_Add your screenshots here!_

---

## 📦 License
MIT (or your preferred license)