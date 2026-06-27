import os

from dotenv import load_dotenv

from src.llm.gemini_client import (
    configure_gemini,
    rank_candidate
)

load_dotenv()

api_key = os.getenv(
    "GEMINI_API_KEY"
)

model = configure_gemini(
    api_key
)


def rerank(prompt):

    result = rank_candidate(

        model,

        prompt

    )

    return result