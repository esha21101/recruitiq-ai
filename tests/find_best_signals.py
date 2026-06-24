from src.parsers.load_candidates import load_candidates

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

best_saved = sorted(
    candidates,
    key=lambda x:
        x["redrob_signals"][
            "saved_by_recruiters_30d"
        ],
    reverse=True
)

print("\nTOP 10 SAVED CANDIDATES\n")

for candidate in best_saved[:10]:

    print(
        candidate["candidate_id"],
        candidate["profile"]["current_title"],
        candidate["redrob_signals"][
            "saved_by_recruiters_30d"
        ]
    )