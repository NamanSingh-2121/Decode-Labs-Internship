"""
Project 2: Data Classification Using AI
DecodeLabs Industrial Training Kit — Batch 2026

Goal: Build a basic classification model using the Iris dataset.
Pipeline (IPO Framework):
    INPUT   -> Load Iris dataset, scale features
    PROCESS -> Train/test split, K-Nearest Neighbors (KNN)
    OUTPUT  -> Confusion Matrix, Accuracy, Precision, Recall, F1 Score
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    accuracy_score,
    f1_score,
)


def load_data():
    """Load and understand the Iris dataset (150 samples, 3 classes, 4 features)."""
    iris = load_iris()
    X, y = iris.data, iris.target
    print("Dataset shape:", X.shape)
    print("Classes:", list(iris.target_names))
    return X, y, iris.target_names


def preprocess(X, y):
    """Split into train/test sets, then scale features (Gatekeeper Rule)."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y, shuffle=True
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, y_train, y_test


def find_best_k(X_train, y_train, X_test, y_test, max_k=20):
    """Tune the engine: test different K values and track error rate."""
    errors = []
    for k in range(1, max_k + 1):
        model = KNeighborsClassifier(n_neighbors=k)
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        errors.append(np.mean(preds != y_test))

    best_k = int(np.argmin(errors)) + 1

    plt.figure(figsize=(7, 4))
    plt.plot(range(1, max_k + 1), errors, marker="o")
    plt.axvline(best_k, color="red", linestyle="--", label=f"Best K = {best_k}")
    plt.title("Error Rate vs. K Value")
    plt.xlabel("K Value")
    plt.ylabel("Error Rate")
    plt.legend()
    plt.tight_layout()
    plt.savefig("k_tuning.png", dpi=150)
    plt.close()

    print(f"\nBest K found: {best_k} (error rate = {errors[best_k - 1]:.3f})")
    return best_k


def train_and_evaluate(X_train, X_test, y_train, y_test, class_names, k):
    """Instantiate, fit, predict — the scikit-learn workflow."""
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)

    acc = accuracy_score(y_test, predictions)
    f1 = f1_score(y_test, predictions, average="weighted")

    print("\n--- Output Validation ---")
    print(f"Accuracy: {acc:.4f}")
    print(f"Weighted F1 Score: {f1:.4f}\n")
    print("Classification Report:")
    print(classification_report(y_test, predictions, target_names=class_names))

    cm = confusion_matrix(y_test, predictions)
    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cm, annot=True, fmt="d", cmap="Blues",
        xticklabels=class_names, yticklabels=class_names,
    )
    plt.title("Confusion Matrix")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.tight_layout()
    plt.savefig("confusion_matrix.png", dpi=150)
    plt.close()

    return model, acc, f1


def main():
    X, y, class_names = load_data()
    X_train, X_test, y_train, y_test = preprocess(X, y)
    best_k = find_best_k(X_train, y_train, X_test, y_test)
    train_and_evaluate(X_train, X_test, y_train, y_test, class_names, best_k)
    print("Saved plots: k_tuning.png, confusion_matrix.png")


if __name__ == "__main__":
    main()
