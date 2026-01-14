from app.evaluator.gemini_evaluator import evaluate as gemini_eval
from app.evaluator.openai_evaluator import evaluate as openai_eval

def evaluate_answer(question: str, answer: str, provider: str = "gemini"):
    if provider == "openai":
        return openai_eval(question, answer)
    return gemini_eval(question, answer)
