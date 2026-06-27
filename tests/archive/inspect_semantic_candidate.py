from src.parsers.load_candidates import (
    load_candidates
)

candidate_id = "CAND_0000847"

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

for candidate in candidates:

    if candidate["candidate_id"] == candidate_id:

        print(
            candidate["profile"]["current_title"]
        )

        print("\nHEADLINE:\n")
        print(
            candidate["profile"]["headline"]
        )

        print("\nSUMMARY:\n")
        print(
            candidate["profile"]["summary"]
        )

        break