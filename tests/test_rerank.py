from src.parsers.job_parser import (
    extract_job_description
)

from src.ranking.select_top_candidates import (
    select_top_candidates
)

from src.llm.candidate_summary import (
    summarize_candidate
)

from src.llm.build_ranking_prompt import (
    build_prompt
)

from src.llm.rerank_top20 import (
    rerank
)

jd = extract_job_description(

"data/raw/job_description.docx"

)

top = select_top_candidates(

"data/raw/candidates.jsonl",

20

)

summary = []

for score, candidate in top:

    summary.append(

        summarize_candidate(

            candidate,

            score

        )

    )

prompt = build_prompt(

    jd,

    summary

)

result = rerank(

    prompt

)

print(result)