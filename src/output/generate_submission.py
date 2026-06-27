import pandas as pd

from src.llm.rerank_top20 import rerank

from src.ranking.select_top_candidates import (
    select_top_candidates
)

from src.llm.candidate_summary import (
    summarize_candidate
)

from src.llm.build_ranking_prompt import (
    build_prompt
)

from src.parsers.job_parser import (
    extract_job_description
)

jd = extract_job_description(

    "data/raw/job_description.docx"

)

top = select_top_candidates(

    "data/raw/candidates.jsonl",

    20

)

summary = []

for hybrid_score,candidate in top:

    item = summarize_candidate(

        candidate,

        hybrid_score

    )

    summary.append(

        item

    )

prompt = build_prompt(

    jd,

    summary

)

results = rerank(

    prompt

)

rows = []

for item in results:

    cid = item["candidate_id"]

    gemini = item["score"]

    reason = item["reason"]

    hybrid = 0

    title = ""

    for score,candidate in top:

        if candidate["candidate_id"] == cid:

            hybrid = score

            title = candidate["profile"]["current_title"]

            break

    final_score = (

        0.75 * gemini

        +

        0.25 * hybrid

    )

    rows.append(

        {

            "candidate_id":

            cid,

            "title":

            title,

            "hybrid_score":

            hybrid,

            "gemini_score":

            gemini,

            "final_score":

            round(

                final_score,

                2

            ),

            "reason":

            reason

        }

    )

df = pd.DataFrame(

    rows

)

df = df.sort_values(

    by="final_score",

    ascending=False

)

df.to_excel(

    "outputs/submission.xlsx",

    index=False

)

print(

df.head()

)

print(

"\nsubmission.xlsx created"

)