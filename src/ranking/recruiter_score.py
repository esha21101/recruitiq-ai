def calculate_recruiter_score(features):

    score = 0

    # Saved by recruiters
    score += features["saved_by_recruiters"] * 0.8

    # Search appearances
    score += features["search_appearance"] * 0.02

    # Interview completion
    score += features["interview_completion"] * 15

    # Offer acceptance
    if features["offer_acceptance"] >= 0:
        score += features["offer_acceptance"] * 10

    # GitHub activity
    github = max(features["github_score"], 0)
    score += github * 0.2

    return round(score, 2)