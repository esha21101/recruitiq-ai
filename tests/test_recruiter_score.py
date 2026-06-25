from src.parsers.load_candidates import load_candidates
from src.ranking.feature_extractor import extract_features
from src.ranking.recruiter_score import calculate_recruiter_score

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

        features = extract_features(candidate)

        score = calculate_recruiter_score(features)

        print("\n" + "=" * 60)

        print(candidate["candidate_id"])
        print(candidate["profile"]["current_title"])

        print("Recruiter Score:", score)