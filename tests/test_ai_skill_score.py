from src.parsers.load_candidates import load_candidates
from src.ranking.ai_skill_score import calculate_ai_skill_score

TARGET_IDS = [
    "CAND_0000031",
    "CAND_0000273",
    "CAND_0000666"
]

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

for candidate in candidates:

    if candidate["candidate_id"] in TARGET_IDS:

        score, matched = calculate_ai_skill_score(candidate)

        print("\n" + "=" * 60)

        print(candidate["candidate_id"])
        print(candidate["profile"]["current_title"])

        print("\nMatched Skills:")

        for skill in matched:
            print("-", skill)

        print("\nAI Skill Score:", score)