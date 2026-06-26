from src.ranking.select_top_candidates import (
    select_top_candidates
)

top = select_top_candidates(
    "data/raw/candidates.jsonl",
    top_n=20
)

for score, candidate in top:

    print(
        candidate["candidate_id"],
        candidate["profile"]["current_title"],
        score
    )