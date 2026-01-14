from pydantic import BaseModel

class EvaluationRequest(BaseModel):
    question: str

class Score(BaseModel):
    clarity: int
    relevance: int
    confidence: int
    overall: float

class EvaluationResponse(BaseModel):
    transcript: str
    scores: Score
    strengths: list[str]
    improvements: list[str]
