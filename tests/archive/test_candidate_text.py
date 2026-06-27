from src.parsers.load_candidates import load_candidates
from src.parsers.candidate_text import build_candidate_text

candidates = load_candidates("data/raw/candidates.jsonl")

candidate = candidates[0]

text = build_candidate_text(candidate)

print(text[:1000])