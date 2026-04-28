import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash-lite")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel(GEMINI_MODEL)


def generate_ai_answer(question: str, context: str) -> str:
    prompt = f"""
You are an AI insurance help center assistant.

Use ONLY the provided context to answer.
Keep the answer short, clear, and structured.

Context:
{context}

User Question:
{question}

Format:
Answer:
Steps:
Important Notes:
"""

    try:
        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 500
            }
        )

        return response.text

    except Exception as ex:
        return (
            "Sorry, I could not generate an AI response right now. "
            "Please try again later.\n\n"
            f"Technical reason: {str(ex)}"
        )