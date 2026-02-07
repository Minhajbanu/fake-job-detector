

import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

from src.database import create_tables
from src.auth import signup_user, login_user
from src.history import save_history, get_history, delete_history
from src.predict import predict_job
from src.preprocess import clean_text
from src.highlight import find_scam_keywords
from src.pdf_report import generate_model_report

create_tables()
st.set_page_config("Fake Job Detector", "🚨")

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if st.session_state.user_id is None:
    st.title("🔐 Login / Signup")

    tab1, tab2 = st.tabs(["Login", "Signup"])

    with tab1:
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            uid = login_user(email, password)
            if uid:
                st.session_state.user_id = uid
                st.success("Logged in successfully")
                st.rerun()
            else:
                st.error("Invalid credentials")

    with tab2:
        email = st.text_input("Signup Email")
        password = st.text_input("Signup Password", type="password")
        if st.button("Signup"):
            if signup_user(email, password):
                st.success("Account created successfully")
            else:
                st.error("User already exists")

    st.stop()

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

page = st.sidebar.selectbox(
    "Menu",
    ["🔍 Job Prediction", "🧾 History", "📊 Model Performance", "🚪 Logout"]
)

if page == "🔍 Job Prediction":
    st.title("🚨 Fake Job Detection")

    job_text = st.text_area("Paste Job Description", height=250)

    if st.button("Analyze"):
        label, confidence, probs = predict_job(
            job_text, model, vectorizer, clean_text
        )

        scam_words = find_scam_keywords(job_text)

        st.subheader("📌 Prediction Result")

        if "Fake" in label:
            st.error(label)
        else:
            st.success(label)

        st.write(f"Confidence: **{confidence:.2f}%**")

        st.subheader("📊 Prediction Probability Distribution")

        prob_data = {
            "Legitimate Job": probs[0],
            "Fake Job": probs[1]
        }

        st.bar_chart(prob_data)

        if scam_words:
            st.warning("⚠️ Suspicious Keywords Detected")
            for w in scam_words:
                st.write("•", w)
        else:
            st.info("No obvious scam keywords detected.")

        save_history(
            st.session_state.user_id,
            job_text,
            label,
            confidence
        )

elif page == "🧾 History":
    st.title("🧾 Prediction History")

    history = get_history(st.session_state.user_id)

    if not history:
        st.info("No history found")
    else:
        for h in history:
            hid, text, label, conf = h
            st.markdown(f"**{label} ({conf:.2f}%)**")
            st.text(text[:250] + "...")
            if st.button("Delete", key=hid):
                delete_history(hid)
                st.rerun()

elif page == "📊 Model Performance":
    st.title("📊 Model Performance Dashboard")

    metrics = joblib.load("model/metrics/metrics.pkl")

    st.subheader("📈 Classification Metrics")

    scores = {
        "Precision": metrics["precision"],
        "Recall": metrics["recall"],
        "F1 Score": metrics["f1"]
    }

    fig, ax = plt.subplots()
    ax.bar(scores.keys(), scores.values())
    ax.set_ylim(0, 1)
    ax.set_ylabel("Score")
    st.pyplot(fig)

    st.subheader("🧮 Confusion Matrix")

    cm = np.array(metrics["confusion_matrix"])

    fig2, ax2 = plt.subplots()
    ax2.imshow(cm)
    ax2.set_xlabel("Predicted")
    ax2.set_ylabel("Actual")
    st.pyplot(fig2)

    st.subheader("🎯 Accuracy")
    st.progress(metrics["accuracy"])
    st.write(f"Accuracy: **{metrics['accuracy']*100:.2f}%**")

    st.subheader("📥 Download Model Evaluation Report")

    if st.button("Generate & Download PDF"):
        report_path = generate_model_report(metrics)
        with open(report_path, "rb") as f:
            st.download_button(
                "📄 Download PDF",
                f,
                file_name="model_performance_report.pdf",
                mime="application/pdf"
            )

else:
    st.session_state.user_id = None
    st.rerun()
