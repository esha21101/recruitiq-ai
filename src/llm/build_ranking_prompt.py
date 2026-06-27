import json


def build_prompt(

    jd,

    candidates

):

    import json


def build_prompt(jd, candidates):

    prompt = f"""

You are a senior recruiter at Redrob.

You already have the Top 20 candidates.

Rank them.

Do NOT reward buzzwords.

Prefer:

career trajectory

retrieval systems

ranking systems

LLM production experience

recommendation systems

behavioral signals

Return ONLY JSON.

Format:

[
{{
"candidate_id":"",

"rank":1,

"score":95,

"reason":""

}}
]

JOB DESCRIPTION

{jd}

CANDIDATES

"""

    for c in candidates:

        prompt += json.dumps(
            c,
            indent=2
        )

        prompt += "\n\n"

    return prompt