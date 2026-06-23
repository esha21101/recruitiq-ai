def build_candidate_text(candidate):
    profile = candidate.get("profile", {})

    text_parts = []

    text_parts.append(profile.get("headline", ""))
    text_parts.append(profile.get("summary", ""))

    for job in candidate.get("career_history", []):
        text_parts.append(job.get("title", ""))
        text_parts.append(job.get("description", ""))

    for skill in candidate.get("skills", []):
        text_parts.append(skill.get("name", ""))

    for cert in candidate.get("certifications", []):
        text_parts.append(cert.get("name", ""))

    return " ".join(text_parts)