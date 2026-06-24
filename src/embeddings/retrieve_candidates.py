import pickle

from sentence_transformers import (
    SentenceTransformer
)

from sklearn.metrics.pairwise import (
    cosine_similarity
)

from src.parsers.load_candidates import (
    load_candidates
)

from src.parsers.job_parser import (
    extract_job_description
)

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

with open(
    "data/candidate_embeddings.pkl",
    "rb"
) as f:

    embeddings = pickle.load(f)

jd = extract_job_description(
    "data/raw/job_description.docx"
)

jd_embedding = model.encode(jd)

results = []

for candidate_id, embedding in embeddings.items():

    similarity = cosine_similarity(
        [jd_embedding],
        [embedding]
    )[0][0]

    results.append(
        (
            candidate_id,
            similarity
        )
    )

results.sort(
    key=lambda x: x[1],
    reverse=True
)

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

candidate_lookup = {
    c["candidate_id"]: c
    for c in candidates
}

print("\nTOP 20 SEMANTIC MATCHES\n")

for candidate_id, score in results[:20]:

    candidate = candidate_lookup[
        candidate_id
    ]

    print(
        candidate_id,
        candidate["profile"][
            "current_title"
        ],
        round(score, 4)
    )