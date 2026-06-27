from src.parsers.load_candidates import (
    load_candidates
)

from src.parsers.candidate_text import (
    build_candidate_text
)

from src.parsers.job_parser import (
    extract_job_description
)

from src.embeddings.semantic_ranker import (
    semantic_similarity
)

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

jd = extract_job_description(
    "data/raw/job_description.docx"
)

candidate = candidates[0]

candidate_text = build_candidate_text(
    candidate
)

score = semantic_similarity(
    jd,
    candidate_text
)

print(
    candidate["candidate_id"]
)

print(
    candidate["profile"]["current_title"]
)

print(
    "\nSimilarity:",
    score
)