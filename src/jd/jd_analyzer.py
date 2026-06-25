import re

AI_SKILLS = [
    "faiss",
    "pinecone",
    "qdrant",
    "weaviate",
    "milvus",
    "langchain",
    "llamaindex",
    "sentence transformers",
    "hugging face transformers",
    "transformers",
    "embeddings",
    "vector search",
    "semantic search",
    "retrieval",
    "ranking",
    "learning to rank",
    "recommendation systems",
    "rag",
    "llm",
    "llms",
    "fine-tuning",
    "mlflow",
    "bentoml",
    "pytorch",
    "tensorflow",
    "opencv",
    "cnn",
    "yolo"
]

JOB_TITLES = [
    "ai engineer",
    "machine learning engineer",
    "ml engineer",
    "recommendation systems engineer",
    "search engineer",
    "nlp engineer",
    "applied scientist",
    "data scientist",
    "ai research engineer",
    "backend engineer",
    "software engineer",
    "data engineer"
]


def analyze_job_description(jd_text):

    text = jd_text.lower()

    skills = []

    for skill in AI_SKILLS:

        if skill in text:
            skills.append(skill)

    titles = []

    for title in JOB_TITLES:

        if title in text:
            titles.append(title)

    experience = None

    match = re.search(r"(\d+)\s*[-–]\s*(\d+)\s*years", text)

    if match:
        experience = (
            int(match.group(1)),
            int(match.group(2))
        )

    return {
        "required_skills": skills,
        "preferred_titles": titles,
        "experience": experience
    }