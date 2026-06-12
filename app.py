from fastapi import FastAPI, UploadFile, File
from dotenv import load_dotenv
import google.generativeai as genai
import json
import fitz
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-flash-lite-latest"
)


app = FastAPI()


document_text = ""



@app.get("/")
async def home():
    return {
        "message": "PDF Question Generator API"
    }


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    global document_text

    if not file.filename.endswith(".pdf"):
        return {
            "error": "Only PDF files are allowed"
        }

    try:

        pdf_bytes = await file.read()

        pdf_document = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        text = ""

        for page in pdf_document:
            text += page.get_text() + "\n"

        document_text = text.strip()

        return {
            "message": "PDF uploaded successfully",
            "chars_loaded": len(document_text)
        }

    except Exception as e:
        return {
            "error": str(e)
        }



@app.post("/generate-questions")
async def generate_questions():

    global document_text

    if not document_text:
        return {
            "error": "No PDF uploaded"
        }

    context = document_text[:4000]

    prompt = f"""
Generate exactly 10 MCQ questions from the lecture notes.

Return ONLY valid JSON.

Format:
[
  {{
    "question": "Question text",
    "options": [
      "Option A",
      "Option B",
      "Option C",
      "Option D"
    ],
    "correct_answer": "Option A"
  }}
]

Rules:
- University level
- No repetition
- 4 options per question
- One correct answer only

Lecture Notes:
{context}
"""

    try:

        response = model.generate_content(prompt)

        clean_text = response.text.replace("```json", "").replace("```", "")

        questions = json.loads(clean_text)

        return {
            "mcq_questions": questions
        }

    except Exception as e:

        import traceback

        return {
            "error_type": str(type(e)),
            "error_message": str(e),
            "trace": traceback.format_exc()
        }