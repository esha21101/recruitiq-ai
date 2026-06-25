import json


def build_prompt(job_description, candidate_text):

    prompt = f"""
You are an expert technical recruiter.

Your task is to evaluate ONE candidate for ONE job.

Job Description:

{job_description}

Candidate Profile:

{candidate_text}

Return ONLY valid JSON.

Example:

{{
    "score": 86,
    "strengths": [
        "...",
        "..."
    ],
    "weaknesses": [
        "...",
        "..."
    ],
    "reason": "..."
}}
"""

    return prompt