from src.ranking.career_score import calculate_career_score
from src.ranking.ai_skill_score import calculate_ai_skill_score
from src.ranking.recruiter_score import calculate_recruiter_score


def calculate_experience_score(years):

    if 5 <= years <= 9:
        return 25

    elif 3 <= years <= 12:
        return 15

    return 5


def calculate_hybrid_score(candidate, features):

    career_score, matched_titles = calculate_career_score(candidate)

    ai_score, matched_skills = calculate_ai_skill_score(candidate)

    recruiter_score = calculate_recruiter_score(features)

    experience_score = calculate_experience_score(
        features["years_experience"]
    )

    final_score = (
        career_score * 0.40
        + ai_score * 0.25
        + recruiter_score * 0.25
        + experience_score * 0.10
    )

    return {
        "final_score": round(final_score, 2),
        "career_score": career_score,
        "ai_skill_score": ai_score,
        "recruiter_score": recruiter_score,
        "experience_score": experience_score,
        "matched_titles": matched_titles,
        "matched_skills": matched_skills
    }