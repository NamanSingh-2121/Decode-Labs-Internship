# Project 2: Data Classification Using AI
**DecodeLabs Industrial Training Kit — Batch 2026**

## Goal
Build a basic classification model using a small dataset (the classic Iris
dataset) with supervised learning.

## Overview
This project follows the **IPO Framework** taught in the kit:

| Stage | What happens |
|---|---|
| **Input** | Load the Iris dataset (150 samples, 3 classes, 4 features) and scale features with `StandardScaler` |
| **Process** | Shuffle + split into train/test sets (80/20), tune K, train a K-Nearest Neighbors (KNN) classifier |
| **Output** | Confusion Matrix, Accuracy, Precision, Recall, F1 Score |

## Key Requirements Covered
- [x] Load and understand a dataset
- [x] Split data into training and testing sets
- [x] Apply a simple classification algorithm (KNN)
- [x] Feature scaling (StandardScaler)
- [x] Model evaluation beyond accuracy (confusion matrix, F1 score)
- [x] K-tuning (elbow method) to pick the best K

## How to Run
```bash
pip install -r requirements.txt
python iris_classification.py
```

## Output
The script prints accuracy, F1 score, and a full classification report to
the console, and saves two plots:
- `k_tuning.png` — error rate across K values, with the optimal K marked
- `confusion_matrix.png` — heatmap of predicted vs. actual classes

## Results
On this run, the model achieved:
- **Accuracy:** ~96.7%
- **Weighted F1 Score:** ~0.97

(Exact numbers can vary slightly depending on the random train/test split.)

## Tech Stack
- Python 3
- scikit-learn
- NumPy
- Matplotlib / Seaborn

## Key Skills Demonstrated
Data handling, supervised learning basics, model training, and validation
through a confusion matrix and F1 score rather than accuracy alone.


