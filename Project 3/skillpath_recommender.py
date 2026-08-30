"""
SkillPath AI - Project 3
Content-based Tech Stack Recommendation Engine

Pipeline:
1. Ingestion  -> load raw_skills.csv
2. Scoring    -> TF-IDF + cosine similarity
3. Sorting    -> highest similarity first
4. Filtering  -> return Top 3 recommendations
"""

import csv
import re
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "raw_skills.csv"


def clean_skill(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip())


def normalize_skills(values):
    """Normalize input and remove duplicate skills without changing user wording."""
    result = []
    seen = set()
    for value in values:
        skill = clean_skill(value)
        key = skill.casefold()
        if skill and key not in seen:
            result.append(skill)
            seen.add(key)
    return result


def load_catalog(path=DATA_FILE):
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def build_similarity_model(catalog):
    # Each role is treated as an item/document in the recommendation catalog.
    documents = [
        f"{row['role']} {row['category']} {row['skills'].replace('|', ' ')}"
        for row in catalog
    ]
    vectorizer = TfidfVectorizer(
        lowercase=True,
        ngram_range=(1, 2),
        sublinear_tf=True
    )
    matrix = vectorizer.fit_transform(documents)
    return vectorizer, matrix


def recommend(user_skills, catalog=None, top_n=3):
    catalog = catalog or load_catalog()
    skills = normalize_skills(user_skills)

    if len(skills) < 3:
        raise ValueError("Please provide at least three distinct skills.")

    vectorizer, item_matrix = build_similarity_model(catalog)
    user_vector = vectorizer.transform([" ".join(skills)])
    similarity_scores = cosine_similarity(user_vector, item_matrix).ravel()

    supplied = {skill.casefold() for skill in skills}
    ranked = []

    for index, score in enumerate(similarity_scores):
        row = catalog[index]
        role_skills = [clean_skill(x) for x in row["skills"].split("|") if clean_skill(x)]
        matched = [skill for skill in role_skills if skill.casefold() in supplied]
        missing = [skill for skill in role_skills if skill.casefold() not in supplied]

        ranked.append({
            "role": row["role"],
            "category": row["category"],
            "score": float(score),
            "matched": matched,
            "recommended_skills": missing[:4],
        })

    ranked.sort(key=lambda item: (-item["score"], item["role"]))
    return ranked[:top_n]


def main():
    print("\n=== SkillPath AI | Project 3 ===")
    print("Content-Based Tech Stack Recommender")
    print("Pipeline: Ingestion -> Scoring -> Sorting -> Filtering")
    raw = input("\nEnter at least 3 skills, separated by commas: ")
    skills = normalize_skills(raw.split(","))

    if len(skills) < 3:
        print("Error: at least three distinct skills are required.")
        return

    print("\nTop 3 recommendations:\n")
    for rank, result in enumerate(recommend(skills), start=1):
        print(f"{rank}. {result['role']} ({result['score']:.0%})")
        print(f"   Category: {result['category']}")
        print(f"   Matching skills: {', '.join(result['matched']) or 'None'}")
        print(f"   Skills to explore: {', '.join(result['recommended_skills']) or 'None'}")


if __name__ == "__main__":
    main()
