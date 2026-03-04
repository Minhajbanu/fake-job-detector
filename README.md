# 🛡️ AI-Based Fake Job Post Detection System

🔗 **Live Demo:**  
https://fake-job-detector-urmvf3h9znetk5nqewdpkf.streamlit.app/

---

## 📌 Overview

The **AI-Based Fake Job Post Detection System** is an intelligent web application designed to detect fraudulent job postings using **Machine Learning** and **Natural Language Processing (NLP)** techniques.

With the rapid expansion of online recruitment platforms, fake job listings have become increasingly common. This system analyzes job descriptions to identify scam patterns such as:

- Misleading or exaggerated language
- Unrealistic salary claims
- Suspicious requirements
- Vague company details

The goal is to enhance trust and safety in online job portals by automatically classifying job posts as **Fake** or **Genuine**.

---

## 🚀 Key Features

- ✅ Detection of fake and genuine job postings  
- 🧠 NLP-based text preprocessing and feature extraction  
- 📊 Machine Learning classification model  
- 🌐 User-friendly interactive web interface  
- ⚡ Real-time prediction results  

---

## 🛠️ Tech Stack

**Programming Language:**  
- Python  

**Machine Learning:**  
- Scikit-learn  

**Natural Language Processing:**  
- Text Cleaning  
- Tokenization  
- Stopword Removal  
- TF-IDF Vectorization  

**Backend:**  
- Flask / FastAPI  

**Frontend:**  
- Streamlit  

**Database:**  
- MongoDB / PostgreSQL  

---

## 🧠 System Architecture

### 🔹 Processing Pipeline

1. User inputs a job description  
2. Text is cleaned and preprocessed using NLP techniques  
3. Features are extracted using **TF-IDF (Term Frequency–Inverse Document Frequency)**  
4. A trained Machine Learning model classifies the job post  
5. The result (**Fake / Genuine**) is displayed in real-time  

---

## 📊 Model Details

### 🔹 Feature Extraction

TF-IDF transforms text into numerical vectors using:

TF = (Term Frequency in Document)  
IDF = log(Total Documents / Documents containing Term)

TF-IDF Score = TF × IDF

This helps highlight important words while reducing the impact of common words.

---

### 🔹 Classification

A supervised machine learning model is trained on labeled job postings to learn scam-related patterns and predict authenticity.

---

## 🔮 Future Enhancements

- 🔹 Integration of Deep Learning models (BERT, Transformers) for improved accuracy  
- 🔹 Job source credibility analysis  
- 🔹 Browser extension for real-time job verification  
- 🔹 Multilingual job post detection  

---

## 🎓 Learning Outcomes

Through this project, I gained:

- Practical experience in **AI-Driven Language Technologies**
- Hands-on implementation of **NLP pipelines**
- Understanding of **feature engineering using TF-IDF**
- Experience building an **end-to-end AI + Full Stack application**
- Model deployment and real-time user interaction design

---

## 👩‍💻 Developed By

**Minhaj Banu**  
AI / NLP Enthusiast  
Focused on Intelligent Language Systems & Real-World AI Applications

---

⭐ If you find this project useful, consider giving it a star!
