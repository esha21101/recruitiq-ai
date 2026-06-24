from src.parsers.load_candidates import load_candidates

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

for candidate in candidates[:10]:

    signals = candidate["redrob_signals"]

    print("\n-------------------")

    print(candidate["candidate_id"])

    print(
        "Title:",
        candidate["profile"]["current_title"]
    )

    print(
        "Saved By Recruiters:",
        signals["saved_by_recruiters_30d"]
    )

    print(
        "Search Appearance:",
        signals["search_appearance_30d"]
    )

    print(
        "Interview Completion:",
        signals["interview_completion_rate"]
    )

    print(
        "Offer Acceptance:",
        signals["offer_acceptance_rate"]
    )

    print(
        "Notice Period:",
        signals["notice_period_days"]
    )