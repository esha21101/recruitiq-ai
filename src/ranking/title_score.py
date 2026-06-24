AI_TITLES = [
    "ai engineer",
    "ml engineer",
    "machine learning engineer",
    "applied scientist",
    "data scientist",
    "search engineer",
    "recommendation systems engineer",
    "recommendation engineer",
    "nlp engineer"
]

NEUTRAL_TITLES = [
    "software engineer",
    "backend engineer",
    "data engineer",
    "platform engineer",
    "senior software engineer"
]


def get_title_score(title):

    title = title.lower()

    for t in AI_TITLES:
        if t in title:
            return 30

    for t in NEUTRAL_TITLES:
        if t in title:
            return 15

    return 0