from sentence_transformers import (
    SentenceTransformer
)

from src.parsers.load_candidates import (
    load_candidates
)

from src.parsers.candidate_text import (
    build_candidate_text
)

import pickle

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

candidates = load_candidates(
    "data/raw/candidates.jsonl"
)

embeddings = {}

for i, candidate in enumerate(
    candidates[:1000]
):

    text = build_candidate_text(
        candidate
    )

    embedding = model.encode(
        text
    )

    embeddings[
        candidate["candidate_id"]
    ] = embedding

    if i % 100 == 0:
        print(i)

with open(
    "data/candidate_embeddings.pkl",
    "wb"
) as f:

    pickle.dump(
        embeddings,
        f
    )

print(
    "\nSaved",
    len(embeddings),
    "embeddings"
)