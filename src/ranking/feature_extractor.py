AI_KEYWORDS = [
    "embedding",
    "embeddings",
    "retrieval",
    "vector",
    "ranking",
    "reranking",
    "llm",
    "fine-tuning",
    "rag",
    "faiss",
    "milvus",
    "pinecone",
    "qdrant",
    "weaviate"
]


def extract_features(candidate):

    profile = candidate.get("profile", {})

    text = ""

    text += profile.get("headline", "") + " "
    text += profile.get("summary", "") + " "

    for job in candidate.get("career_history", []):
        text += job.get("description", "") + " "

    text = text.lower()

    features = {
        "candidate_id": candidate["candidate_id"],

        "current_title":
            profile.get("current_title", ""),

        "years_experience":
            profile.get("years_of_experience", 0),

        "open_to_work":
            candidate["redrob_signals"].get(
                "open_to_work_flag",
                False
            ),

        "github_score":
            candidate["redrob_signals"].get(
                "github_activity_score",
                -1
            ),

        "response_rate":
            candidate["redrob_signals"].get(
                "recruiter_response_rate",
                0
            )
    }

    for keyword in AI_KEYWORDS:

        features[f"has_{keyword}"] = (
            keyword in text
        )

    return features