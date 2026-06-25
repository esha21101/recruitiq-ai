CAREER_SCORES = {
    "recommendation systems engineer": 25,
    "search engineer": 25,

    "ai engineer": 22,
    "lead ai engineer": 24,
    "senior ai engineer": 24,
    "staff machine learning engineer": 25,

    "machine learning engineer": 22,
    "ml engineer": 22,
    "applied ml engineer": 20,
    "ai research engineer": 20,
    "nlp engineer": 20,

    "applied scientist": 18,
    "senior applied scientist": 20,
    "data scientist": 16,

    "backend engineer": 8,
    "software engineer": 8,
    "senior software engineer": 10,
    "data engineer": 8
}


def calculate_career_score(candidate):

    score = 0

    matched_titles = []

    jobs = candidate.get(
        "career_history",
        []
    )

    for job in jobs:

        title = job.get(
            "title",
            ""
        ).lower()

        for key in CAREER_SCORES:

            if key in title:

                score += CAREER_SCORES[key]
                matched_titles.append(title)

                break

    return score, matched_titles