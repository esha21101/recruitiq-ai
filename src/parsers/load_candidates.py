import json

def load_candidates(file_path):
    candidates = []

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            candidates.append(json.loads(line))

    return candidates


if __name__ == "__main__":
    candidates = load_candidates("data/raw/candidates.jsonl")

    print(f"Total candidates: {len(candidates)}")

    first = candidates[0]

    print("\nCandidate ID:")
    print(first["candidate_id"])

    print("\nCurrent Title:")
    print(first["profile"]["current_title"])

    print("\nYears Experience:")
    print(first["profile"]["years_of_experience"])