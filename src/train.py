


import os
import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)

from src.preprocess import clean_text


os.makedirs("model", exist_ok=True)
os.makedirs("model/metrics", exist_ok=True)

df = pd.read_csv("data/fake_job_postings.csv")

df["text"] = (
    df["title"].fillna("") + " " +
    df["description"].fillna("") + " " +
    df["requirements"].fillna("")
)

df["text"] = df["text"].apply(clean_text)

X = df["text"]
y = df["fraudulent"]

vectorizer = TfidfVectorizer(max_features=5000)
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    results[name] = {
        "model": model,
        "accuracy": accuracy_score(y_test, preds),
        "precision": precision_score(y_test, preds),
        "recall": recall_score(y_test, preds),
        "f1": f1_score(y_test, preds),
        "confusion_matrix": confusion_matrix(y_test, preds)
    }

best_model_name = max(results, key=lambda x: results[x]["accuracy"])
best = results[best_model_name]

joblib.dump(best["model"], "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

joblib.dump({
    "model_name": best_model_name,
    "accuracy": best["accuracy"],
    "precision": best["precision"],
    "recall": best["recall"],
    "f1": best["f1"],
    "confusion_matrix": best["confusion_matrix"]
}, "model/metrics/metrics.pkl")

print(" Training complete")
print(f" Best Model: {best_model_name}")
print(f" Accuracy : {best['accuracy'] * 100:.2f}%")
print(f" Precision: {best['precision'] * 100:.2f}%")
print(f" Recall   : {best['recall'] * 100:.2f}%")
print(f" F1 Score : {best['f1'] * 100:.2f}%")
