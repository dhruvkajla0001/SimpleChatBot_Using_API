<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<!--   <title>BuddyBot - README</title> -->
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">

</head>
<body>
  <h1>🤖 BuddyBot</h1>
  <p class="badge">Your Learning Friend</p>

  <p><strong>BuddyBot</strong> is a smart and engaging web-based assistant built using Flask. It supports real-time chat, speech recognition, file summarization (PDF, TXT, DOCX), and a stylish dark-themed UI.</p>

  <h2>✨ Features</h2>
  <ul>
    <li>🎙️ <strong>Speech-to-Text</strong> input using browser’s native API</li>
    <li>📄 <strong>File Upload</strong> (.pdf, .txt, .docx) and AI Summarization</li>
    <li>📚 <strong>Chat History</strong> tracking with styling</li>
    <li>⚡ Powered by <code>Gemini</code> (Google Generative AI)</li>
    <li>🌈 Animated pastel background and smooth transitions</li>
  </ul>

  <h2>🛠 Technologies Used</h2>
  <ul>
    <li>Python + Flask</li>
    <li>HTML + CSS + JavaScript</li>
    <li>Gemini Generative AI API</li>
    <li>PyPDF2, python-docx for file reading</li>
  </ul>

  <h2>📂 Project Structure</h2>
  <pre>
├── app.py
├── config.py
├── chatbot.py
├── utils.py
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── requirements.txt
  </pre>

  <h2>🚀 How to Run</h2>
  <pre>
# Clone the repo
git clone https://github.com/yourusername/buddybot

# Navigate to project
cd buddybot

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GEMINI_API_KEY=your_key_here

# Run the app
python app.py
  </pre>
  <h2>output</h2>
![Screenshot 2025-06-26 153703](https://github.com/user-attachments/assets/38457dc5-a360-4e66-8a68-4a580b5e1a5b)



  <h2>🔐 Environment Variables</h2>
  <ul>
    <li><code>GEMINI_API_KEY</code> – Your Google Gemini AI key</li>
  </ul>

  <h2>📬 Contact</h2>
  <p>Made with 💙 by <strong>Dhruv Kajla</strong>. Reach out via <a href="dhruvkajla@gmail.com">email</a> or follow on <a href="https://github.com/dhruvkajla0001" target="_blank">GitHub</a>.</p>
   <p>Made with 💙 by <strong>Mukund Malik</strong>. Reach out via <a href="mukund3818.be22@chitkara.edu.in">email</a> or follow on <a href="https://github.com/Mukusick2" target="_blank">GitHub</a>.</p>
</body>
</html>
