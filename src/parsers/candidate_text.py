def build_candidate_text(candidate):

    profile = candidate.get(
        "profile",
        {}
    )

    parts = []

    # Current role

    parts.append(
        profile.get(
            "current_title",
            ""
        )
    )

    # Career history

    for job in candidate.get(
        "career_history",
        []
    ):

        parts.append(
            job.get(
                "title",
                ""
            )
        )

        parts.append(
            job.get(
                "description",
                ""
            )
        )

    # Skills

    for skill in candidate.get(
        "skills",
        []
    ):

        parts.append(
            skill.get(
                "name",
                ""
            )
        )

    # Certifications

    for cert in candidate.get(
        "certifications",
        []
    ):

        parts.append(
            cert.get(
                "name",
                ""
            )
        )

    return " ".join(parts)