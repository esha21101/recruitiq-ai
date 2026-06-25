from src.parsers.load_candidates import load_candidates

from src.ranking.career_score import (
    calculate_career_score
)

TARGET_IDS = [
    "CAND_0000031",
    "CAND_0000273",
    "CAND_0000666",
    "CAND_0000967"
]

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

for candidate in candidates:

    if candidate["candidate_id"] in TARGET_IDS:

        score, matched = calculate_career_score(
            candidate
        )

        print("\n" + "=" * 70)

        print(
            candidate["candidate_id"]
        )

        print(
            candidate["profile"]["current_title"]
        )

        print("\nMatched Career Titles:")

        for title in matched:

            print("-", title)

        print(
            "\nCareer Score:",
            score
        )