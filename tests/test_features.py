from src.parsers.load_candidates import load_candidates
from src.ranking.feature_extractor import extract_features

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

features = extract_features(
    candidates[0]
)

for k, v in features.items():
    print(k, ":", v)