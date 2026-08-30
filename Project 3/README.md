# SkillPath AI — Project 3: Tech Stack Recommender

SkillPath AI is a simple **content-based recommendation system** built for Project 3.
It maps a user's technical skills to relevant career paths using **TF-IDF weighting
and cosine similarity**.

## Project 3 pipeline

**1. Ingestion**  
Load the career/skill catalog from `raw_skills.csv`.

**2. Scoring**  
Convert the user's skills and career items into TF-IDF vectors and calculate
cosine similarity.

**3. Sorting**  
Rank all career items from the highest similarity score to the lowest.

**4. Filtering**  
Return only the **Top 3** highest-scoring recommendations.

## Input rule

The interface and Python program require **at least 3 distinct skills**, matching
the project guidance.

Example:

`Python, SQL, Machine Learning`

## Output

Each recommendation includes:
- Career path
- Category
- Similarity/match percentage
- Matching skills
- Skills worth exploring next

## Content-based approach

The recommendation does not use other users' history. Each career role is treated
as an item described by its own attributes/skills. The user's profile is compared
directly with those item attributes.

## Run

```bash
pip install -r requirements.txt
python skillpath_recommender.py
```

The web demo is `index.html` and can be opened directly in a browser.

## Files

- `index.html` — interactive demonstration
- `skillpath_recommender.py` — Python recommendation engine
- `raw_skills.csv` — career-role/skill catalog
- `requirements.txt` — dependency
- `README.md` — project documentation
