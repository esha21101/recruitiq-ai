# RecruitIQ-AI

AI-powered candidate ranking system built for the Redrob Data & AI Challenge.

---

# Problem Statement

Recruiters review hundreds or thousands of profiles every day and often miss strong candidates because traditional Applicant Tracking Systems rely heavily on keyword matching.

RecruitIQ-AI aims to rank candidates the way an experienced recruiter would by understanding:

- Career trajectory
- Technical depth
- AI-specific expertise
- Recruiter engagement signals
- Candidate behavior
- Job description intent

rather than simply matching keywords.

---

# Dataset

The project uses the Redrob challenge dataset consisting of:

- 100,000 candidate profiles
- Career histories
- Skills
- Behavioral signals
- Platform activity
- Recruiter engagement metrics
- Job descriptions

---

# Approach

RecruitIQ-AI follows a hybrid ranking pipeline.

## Stage 1 — Job Description Understanding

The job description is analyzed to identify:

- required skills
- preferred titles
- experience range
- role expectations

Implemented in:

```text
src/jd/jd_analyzer.py
```

Extracted information includes:

```python
required_skills

preferred_titles

experience_range
```

---

## Stage 2 — Hybrid Ranking

Each candidate receives a score based on multiple dimensions.

### Career Score

Measures relevance of previous roles.

Examples:

- Search Engineer
- Recommendation Systems Engineer
- ML Engineer
- Applied ML Engineer
- AI Research Engineer

Weight:

```text
35%
```

Implemented in:

```text
src/ranking/career_score.py
```

---

### AI Skill Score

Measures expertise in modern AI infrastructure.

Examples:

- FAISS
- Pinecone
- Qdrant
- Weaviate
- Milvus
- Sentence Transformers
- Embeddings
- Information Retrieval
- LangChain
- LlamaIndex
- RAG
- Fine-tuning LLMs
- Learning to Rank
- MLflow

Weight:

```text
30%
```

Implemented in:

```text
src/ranking/ai_skill_score.py
```

---

### Recruiter Signal Score

Behavioral features used include:

- Saved by recruiters
- Search appearances
- Interview completion
- Offer acceptance
- Github activity
- Profile engagement

Weight:

```text
20%
```

Implemented in:

```text
src/ranking/recruiter_score.py
```

---

### Experience Score

Measures alignment with the required experience range.

Weight:

```text
15%
```

---

## Stage 3 — Hybrid Ranker

Combines:

- Career Score
- AI Skill Score
- Recruiter Signals
- Experience Score

Implemented in:

```text
src/ranking/hybrid_ranker.py
```

Produces an initial ranking across the entire dataset.

---

## Stage 4 — Candidate Selection

Top candidates are selected using the Hybrid Ranker.

Implemented in:

```text
src/ranking/select_top_candidates.py
```

---

## Stage 5 — LLM Re-ranking

Gemini acts as an AI recruiter.

It evaluates:

- career progression
- ranking experience
- retrieval expertise
- production ML experience
- vector database experience
- recommendation systems
- evaluation frameworks
- AI engineering maturity

Implemented in:

```text
src/llm/rerank_top20.py
```

---

## Stage 6 — Explainability

Gemini produces:

- rank
- score
- strengths
- weaknesses
- reasoning

This makes the ranking process transparent and interpretable.

Example:

```json
{
 "candidate_id":"CAND_0071974",

 "score":95,

 "reason":"Exceptional alignment with retrieval, ranking, and AI systems."
}
```

---

## Stage 7 — Submission Generation

Final rankings are exported automatically.

Implemented in:

```text
src/output/generate_submission.py
```

Output:

```text
outputs/submission.xlsx
```

---

# Architecture

```text
Job Description
       │
       ▼

JD Analyzer

       │
       ▼

Hybrid Ranker

├── Career Score

├── AI Skill Score

├── Recruiter Signals

├── Experience Score

       │
       ▼

Top Candidates

       │
       ▼

Gemini Re-ranking

       │
       ▼

Explainability Layer

       │
       ▼

submission.xlsx
```

---

# Repository Structure

```text
RecruitIQ-AI/

src/

    embeddings/

    jd/

    llm/

    parsers/

    ranking/

    output/

tests/

outputs/

README.md

requirements.txt

.gitignore
```

---

# Tech Stack

### Language

Python

---

### LLM

Gemini 2.5 Flash

---

### NLP

Sentence Transformers

---

### Data Processing

Pandas

NumPy

OpenPyXL

---

### ML

Scikit-Learn

Transformers

HuggingFace

---

# Installation

Clone the repository

```bash
git clone <repo_url>

cd RecruitIQ-AI
```

Create environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Project

Job Description Analysis

```bash
python -m tests.test_jd_analyzer
```

Hybrid Ranker

```bash
python -m tests.test_hybrid_ranker
```

Gemini Integration

```bash
python -m tests.test_gemini
```

Gemini Re-ranking

```bash
python -m tests.test_rerank
```

Generate Final Submission

```bash
python -m src.output.generate_submission
```

---

# Results

RecruitIQ-AI successfully:

✅ Processes 100,000 candidates

✅ Understands job requirements

✅ Scores candidates using multiple dimensions

✅ Uses LLM reasoning for re-ranking

✅ Produces recruiter-style explanations

✅ Generates a ranked submission file

---

# Deliverables

Included in the repository:

- Source code
- README
- submission.xlsx
- PPT/PDF
- Architecture diagram

---

# Future Improvements

Potential future enhancements:

- Cross-encoder reranking
- Learning-to-rank models
- FAISS indexing
- Reinforcement learning from recruiter feedback
- Interactive recruiter dashboard
- Candidate similarity search

---

# Authors

Developed as part of the Redrob Data & AI Challenge.

RecruitIQ-AI