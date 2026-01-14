from fastapi import FastAPI, UploadFile, File
from app.whisper_service import transcribe_audio
from app.evaluator import evaluate_answer
import shutil, uuid

app = FastAPI(title="AI Interview Answer Evaluator")

@app.post("/evaluate")
async def evaluate_interview(
    question: str,
    provider: str = "gemini",
    audio: UploadFile = File(...)
):
    temp_file = f"temp_{uuid.uuid4()}.wav"
    with open(temp_file, "wb") as f:
        shutil.copyfileobj(audio.file, f)

    transcript = transcribe_audio(temp_file)
    result = evaluate_answer(question, transcript, provider)

    clarity = result["clarity"]
    relevance = result["relevance"]
    confidence = result["confidence"]

    overall = round(
        0.35 * relevance + 0.35 * clarity + 0.30 * confidence, 2
    )

    return {
        "transcript": transcript,
        "scores": {
            "clarity": clarity,
            "relevance": relevance,
            "confidence": confidence,
            "overall": overall
        },
        "strengths": result["strengths"],
        "improvements": result["improvements"]
    }
