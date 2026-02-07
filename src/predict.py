# def predict_job(text, model, vectorizer, clean_func):
#     cleaned = clean_func(text)
#     vector = vectorizer.transform([cleaned])

#     prediction = model.predict(vector)[0]
#     probability = model.predict_proba(vector)[0]

#     confidence = max(probability) * 100

#     label = "🚨 Fake Job Posting" if prediction == 1 else " Legitimate Job Posting"
#     return label, confidence

import numpy as np

def predict_job(text, model, vectorizer, clean_text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])

    probs = model.predict_proba(vec)[0]
    pred = np.argmax(probs)

    label = "🚨 Fake Job" if pred == 1 else "✅ Legitimate Job"
    confidence = probs[pred] * 100

    return label, confidence, probs
