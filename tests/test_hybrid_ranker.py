from src.parsers.load_candidates import load_candidates
from src.ranking.feature_extractor import extract_features
from src.ranking.hybrid_ranker import calculate_hybrid_score

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

        result = calculate_hybrid_score(
            candidate,
            features
        )

        print("\n" + "=" * 80)

        print(candidate["candidate_id"])
        print(candidate["profile"]["current_title"])

        print("\nHybrid Result")

        for key, value in result.items():
            print(f"{key}: {value}")