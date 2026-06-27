def summarize_candidate(candidate, score):

    profile = candidate["profile"]

    career = candidate.get(
        "career_history",
        []
    )

    skills = candidate.get(
        "skills",
        []
    )

    signals = candidate.get(
        "redrob_signals",
        {}
    )

    titles = []

    for job in career:

        titles.append(
            job["title"]
        )

    skill_names = []

    for skill in skills[:10]:

        skill_names.append(
            skill["name"]
        )

    return {

        "candidate_id":

        candidate["candidate_id"],

        "title":

        profile["current_title"],

        "experience":

        profile[
            "years_of_experience"
        ],

        "career":

        titles,

        "skills":

        skill_names,

        "saved":

        signals.get(
            "saved_by_recruiters_30d",
            0
        ),

        "hybrid_score":

        round(score,2)

    }