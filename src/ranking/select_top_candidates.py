from src.parsers.load_candidates import load_candidates
from src.ranking.feature_extractor import extract_features
from src.ranking.hybrid_ranker import calculate_hybrid_score


def select_top_candidates(path, top_n=100):

    candidates = load_candidates(path)

    ranked = []

    for candidate in candidates:

        features = extract_features(candidate)

        result = calculate_hybrid_score(
            candidate,
            features
        )

        ranked.append(
            (
                result["final_score"],
                candidate
            )
        )

    ranked.sort(
        reverse=True,
        key=lambda x: x[0]
    )

    return ranked[:top_n]