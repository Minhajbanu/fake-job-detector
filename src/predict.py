

import numpy as np

def predict_job(text, model, vectorizer, clean_text):
    cleaned = clean_text(text)
    vec = vectorizer.transform([cleaned])

    probs = model.predict_proba(vec)[0]
    pred = np.argmax(probs)

    label = "🚨 Fake Job" if pred == 1 else "✅ Legitimate Job"
    confidence = probs[pred] * 100

    return label, confidence, probs
