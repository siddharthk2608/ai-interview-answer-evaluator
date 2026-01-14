# 🎙️ AI Interview Answer Evaluator

An AI-powered system that evaluates **interview answers from audio** and generates **structured feedback and scores** based on clarity, relevance, and confidence.

The project is **automation-first**, has a **minimal UI**, and is designed for real-world use by **recruiters, candidates, and interview coaching platforms**.

---

## 🚀 Features

- 🎧 Upload interview answers as audio (`.wav`, `.mp3`, `.m4a`)
- 🧠 Speech-to-text using Whisper (faster-whisper)
- 📊 LLM-based evaluation using Google Gemini (OpenAI optional)
- ✅ Scores for:
  - Clarity
  - Relevance
  - Confidence
  - Overall score
- 📝 Actionable strengths & improvement suggestions
- 🔌 Clean REST API built with FastAPI
- 🎨 Lightweight Streamlit UI (frontend only, backend unchanged)

---

## 🏗️ Architecture Overview

```
Audio Input
    ↓
Speech-to-Text (Whisper)
    ↓
Text Cleaning & Normalization
    ↓
LLM Evaluation (Gemini / OpenAI)
    ↓
Scoring Engine
    ↓
JSON Feedback (FastAPI API)
    ↓
Streamlit UI (Optional)
```

---

## 🛠 Tech Stack

### Backend
- Python
- FastAPI
- Whisper (faster-whisper)
- Google Gemini (LLM)
- Optional: OpenAI (fallback)

### Frontend
- Streamlit

### Dev & Infra
- FFmpeg
- Uvicorn
- Watchdog

---

## 📂 Project Structure

```
ai-interview-answer-evaluator/
│
├── app/
│   ├── main.py
│   ├── whisper_service.py
│   ├── evaluator/
│   │   ├── gemini_evaluator.py
│   │   ├── openai_evaluator.py
│   │   └── __init__.py
│
├── UI/
│   ├── ui.py
├── requirements.txt
├── README.md
└── sample_audio/
```

---

## ⚙️ Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/your-username/ai-interview-answer-evaluator.git
cd ai-interview-answer-evaluator
```

### Create & Activate Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Install FFmpeg
```bash
brew install ffmpeg
```

### Set Environment Variables
```bash
export GOOGLE_API_KEY="your_gemini_api_key"
```

---

## ▶️ Run the Backend API
```bash
uvicorn app.main:app --reload
```

Swagger UI:
```
http://127.0.0.1:8000/docs
```

---

## 🎨 Run the Streamlit UI
```bash
streamlit run ui.py
```

---

## 📤 API Usage Example
```bash
curl -X POST "http://127.0.0.1:8000/evaluate?question=Tell%20me%20about%20a%20challenging%20project"   -F "audio=@answer.wav"
```

---
