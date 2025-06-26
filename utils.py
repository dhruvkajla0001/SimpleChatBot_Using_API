import PyPDF2
import docx
import google.generativeai as genai
from config import GEMINI_API_KEY

# ✅ Configure Gemini API using key from config
genai.configure(api_key=GEMINI_API_KEY)

# ---------- File Reading Helpers ----------

def read_text_file(file_stream):
    file_stream.seek(0)
    return file_stream.read().decode('utf-8')


def read_pdf_file(file_stream):
    file_stream.seek(0)
    try:
        reader = PyPDF2.PdfReader(file_stream)
        return "\n".join(page.extract_text() or "" for page in reader.pages).strip()
    except Exception:
        return "⚠️ Could not read the PDF. It might be corrupted or encrypted."


def read_docx_file(file_stream):
    file_stream.seek(0)
    try:
        doc = docx.Document(file_stream)
        return "\n".join(p.text for p in doc.paragraphs).strip()
    except Exception:
        return "⚠️ Could not read the DOCX file."


def extract_text_from_file(file_storage):
    filename = file_storage.filename.lower()
    stream = file_storage.stream

    if filename.endswith('.txt'):
        return read_text_file(stream)
    elif filename.endswith('.pdf'):
        return read_pdf_file(stream)
    elif filename.endswith('.docx'):
        return read_docx_file(stream)
    else:
        raise ValueError("❌ Unsupported file format. Please upload a .txt, .pdf, or .docx file.")


# ---------- Summarization Logic ----------

def summarize_text(text):
    if not text.strip():
        return "⚠️ The uploaded file is empty or unreadable."

    prompt = (
        "You're a helpful assistant. Please summarize the following text clearly in bullet points:\n\n"
        f"{text}\n\n"
        "📌 Summary:"
    )

    try:
        model = genai.GenerativeModel("models/gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error during summarization: {str(e)}"
