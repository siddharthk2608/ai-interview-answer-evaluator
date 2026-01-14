import openai
import json
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def evaluate(question: str, answer: str):
    prompt = f"""
You are an interview evaluator.

Question:
{question}

Answer:
{answer}

Evaluate on clarity, relevance, confidence (0-10).
Return ONLY valid JSON with strengths and improvements.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return json.loads(response.choices[0].message.content)
