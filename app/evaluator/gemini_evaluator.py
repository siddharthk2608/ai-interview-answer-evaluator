import google.generativeai as genai
import json
import os
import re

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel(
    # model_name="gemini-1.5-flash",
    model_name="gemini-2.5-flash",
    generation_config={
        "temperature": 0,
        "response_mime_type": "application/json"
    }
)

def evaluate(question: str, answer: str):
    prompt = f"""
You are an interview evaluator.

Question:
{question}

Answer:
{answer}

Evaluate on:
1. Clarity (0-10)
2. Relevance (0-10)
3. Confidence (0-10)

Return ONLY valid JSON:
{{
  "clarity": number,
  "relevance": number,
  "confidence": number,
  "strengths": ["", ""],
  "improvements": ["", ""]
}}
"""

    response = model.generate_content(prompt)
    text = response.text.strip()

    match = re.search(r"\{.*\}", text, re.DOTALL)
    if not match:
        raise ValueError("Invalid JSON from Gemini")

    return json.loads(match.group())
