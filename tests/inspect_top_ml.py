from src.parsers.load_candidates import (
    load_candidates
)

TARGET_IDS = [
    "CAND_0000273",
    "CAND_0000666",
    "CAND_0000031"
]

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

for candidate in candidates:

    if candidate["candidate_id"] in TARGET_IDS:

        print("\n" + "=" * 80)

        print(
            "Candidate ID:",
            candidate["candidate_id"]
        )

        print(
            "Title:",
            candidate["profile"]["current_title"]
        )

        print(
            "Experience:",
            candidate["profile"]["years_of_experience"]
        )

        print("\nSKILLS:")

        for skill in candidate.get(
            "skills",
            []
        ):
            print(
                "-",
                skill["name"]
            )

        print("\nCAREER HISTORY:")

        for job in candidate.get(
            "career_history",
            []
        ):

            print(
                "-",
                job["title"]
            )

        print("\nSUMMARY:")

        print(
            candidate["profile"]["summary"]
        )

        print("\nRECRUITER SIGNALS:")

        signals = candidate[
            "redrob_signals"
        ]

        print(
            "Saved:",
            signals[
                "saved_by_recruiters_30d"
            ]
        )

        print(
            "Search Appearance:",
            signals[
                "search_appearance_30d"
            ]
        )

        print(
            "Interview Completion:",
            signals[
                "interview_completion_rate"
            ]
        )

        print(
            "Offer Acceptance:",
            signals[
                "offer_acceptance_rate"
            ]
        )

        print(
            "Github Score:",
            signals[
                "github_activity_score"
            ]
        )