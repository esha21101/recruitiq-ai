AI_SKILLS = {
    "faiss": 12,
    "pinecone": 12,
    "qdrant": 12,
    "weaviate": 12,
    "milvus": 12,

    "sentence transformers": 10,
    "hugging face transformers": 10,
    "transformers": 8,

    "embeddings": 10,
    "vector search": 10,
    "semantic search": 10,
    "information retrieval": 12,

    "recommendation systems": 15,
    "learning to rank": 15,
    "ranking": 10,
    "retrieval": 10,

    "rag": 8,
    "langchain": 8,
    "llamaindex": 8,

    "mlflow": 6,
    "bentoml": 6,
    "lora": 6,

    "fine-tuning llms": 10,
    "llms": 6
}


def calculate_ai_skill_score(candidate):

    score = 0

    matched_skills = []

    skills = candidate.get("skills", [])

    for skill in skills:

        name = skill["name"].lower()

        if name in AI_SKILLS:

            score += AI_SKILLS[name]
            matched_skills.append(name)

    return score, matched_skills