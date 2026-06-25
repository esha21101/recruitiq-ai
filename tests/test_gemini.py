import os

from dotenv import load_dotenv

from src.llm.gemini_client import (
    configure_gemini,
    rank_candidate
)

from src.llm.gemini_ranker import build_prompt

from src.parsers.job_parser import extract_job_description
from src.parsers.load_candidates import load_candidates
from src.parsers.candidate_text import build_candidate_text

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

model = configure_gemini(api_key)

jd = extract_job_description(
    "data/raw/job_description.docx"
)

candidate = load_candidates(
    "data/raw/candidates.jsonl"
)[30]

candidate_text = build_candidate_text(
    candidate
)

prompt = build_prompt(
    jd,
    candidate_text
)

result = rank_candidate(
    model,
    prompt
)

print(result)