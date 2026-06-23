from src.parsers.load_candidates import load_candidates

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

target_id = "CAND_0000967"

for candidate in candidates:

    if candidate["candidate_id"] == target_id:

        print(candidate)

        break