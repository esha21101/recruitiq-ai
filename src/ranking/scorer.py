def score_candidate(features):

    score = 0

    # Experience
    exp = features["years_experience"]

    if 5 <= exp <= 9:
        score += 25
    elif 3 <= exp <= 12:
        score += 15

    # AI Skills
    ai_keywords = [
        "embeddings",
        "retrieval",
        "ranking",
        "llm",
        "rag",
        "faiss",
        "milvus",
        "pinecone",
        "qdrant",
        "weaviate"
    ]

    for keyword in ai_keywords:
        key = f"has_{keyword}"

        if key in features and features[key]:
            score += 8

    # Behavioral Signals

    if features["open_to_work"]:
        score += 10

    score += features["response_rate"] * 10

    github = max(features["github_score"], 0)

    score += github * 0.2

    return round(score, 2)