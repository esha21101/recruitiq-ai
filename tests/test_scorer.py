from src.parsers.load_candidates import load_candidates
from src.ranking.feature_extractor import extract_features
from src.ranking.scorer import score_candidate

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

candidate = candidates[0]

features = extract_features(candidate)

score = score_candidate(features)

print(features)
print("\nScore:", score)