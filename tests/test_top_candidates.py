from src.parsers.load_candidates import load_candidates
from src.ranking.feature_extractor import extract_features
from src.ranking.scorer import score_candidate

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

results = []

for candidate in candidates[:1000]:
    features = extract_features(candidate)

    score = score_candidate(features)

    results.append(
        (
            candidate["candidate_id"],
            candidate["profile"]["current_title"],
            candidate["profile"]["years_of_experience"],
            score
        )
    )

results.sort(
    key=lambda x: x[3],
    reverse=True
)

for row in results[:20]:
    print(row)