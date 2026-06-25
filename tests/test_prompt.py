from src.parsers.job_parser import extract_job_description
from src.parsers.load_candidates import load_candidates
from src.parsers.candidate_text import build_candidate_text

from src.llm.gemini_ranker import build_prompt

jd = extract_job_description(
    "data/raw/job_description.docx"
)

candidate = load_candidates(
    "data/raw/candidates.jsonl"
)[30]

text = build_candidate_text(candidate)

prompt = build_prompt(
    jd,
    text
)

print(prompt)