
# PDF Question Generator API

AI-powered API that generates MCQ questions from uploaded PDF lecture notes using FastAPI and Google Gemini.

---

## Features

- Upload PDF files
- Extract text from PDF
- Generate MCQ questions automatically
- JSON API responses
- FastAPI Swagger UI support

---

## Technologies Used

- FastAPI
- Google Gemini API
- PyMuPDF (fitz)
- Python Dotenv
- Uvicorn

---

## Installation

### 1) Clone Project

```bash
git clone <your-repo-url>
cd <project-folder>
````

### 2) Create Virtual Environment

```bash
python -m venv venv
```

### 3) Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create .env File

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_api_key_here
```

Get your API key from:

[https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

---

## Run the Server

```bash
uvicorn app:app --reload
```

If uvicorn is not recognized:

```bash
python -m uvicorn main:app --reload
```

---

## API Endpoints

### Home Endpoint

```http
GET /
```

Response:

```json
{
  "message": "PDF Question Generator API"
}
```

---

### Upload PDF

```http
POST /upload-pdf
```

Form Data:

| Key  | Type |
| ---- | ---- |
| file | PDF  |

Response:

```json
{
  "message": "PDF uploaded successfully",
  "chars_loaded": 5000
}
```

---

### Generate Questions

```http
POST /generate-questions
```

Response:

```json
{
  "mcq_questions": [
    {
      "question": "What is Machine Learning?",
      "options": [
        "Option A",
        "Option B",
        "Option C",
        "Option D"
      ],
      "correct_answer": "Option A"
    }
  ]
}
```

---

## Swagger Documentation

After running the server:

```text
http://127.0.0.1:8000/docs
```

---

## Example Workflow

1. Upload PDF using `/upload-pdf`
2. Generate questions using `/generate-questions`
3. Receive MCQ questions in JSON format

---

## Common Errors

### 429 RESOURCE_EXHAUSTED

Your Gemini quota has been exceeded.

Solution:

* Wait for quota reset
* Upgrade Gemini API plan

---

### Model Not Found

Replace:

```python
"gemini-flash-lite-latest"
```

With:

```python
"gemini-1.5-flash"
```

or:

```python
"gemini-2.0-flash"
```

---

## Author

Developed using FastAPI and Gemini AI.

````

---

