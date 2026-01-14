# 📊 Stock Market Sentiment Analysis using Domain-Adaptive Fine-Tuning (DAFT)

## 📌 Overview
This project focuses on extracting **high-quality financial sentiment signals** from social media data (X / Twitter) to support stock market analysis.  
Unlike typical sentiment analysis projects, this work introduces a **Domain-Adaptive Fine-Tuning (DAFT)** stage to filter noisy, spam-heavy tweets **before** applying sentiment models.

The motivation is simple:
> Raw social media data is extremely noisy. Without filtering, sentiment models produce unreliable signals.

This repository demonstrates a **research-inspired, industry-style NLP pipeline** designed for real-world financial text.

---

## 🚀 Key Contributions
- ✅ Uses **X API v2** for legal and stable tweet collection
- ✅ Introduces a **Tweet Quality Classifier** trained via **Domain-Adaptive Fine-Tuning (DAFT)**
- ✅ Applies **weak supervision** to build a custom dataset
- ✅ Separates **quality filtering** from **sentiment analysis**
- ✅ Designed for **financial Twitter discourse**, not generic text

---

