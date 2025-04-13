# 👗 Fashion Product Recommendation System

Welcome to the **Fashion Product Recommendation System** – a smart tool that suggests similar fashion products based on your input using Natural Language Processing and machine learning!

## Screenshorts

![Home page](https://github.com/user-attachments/assets/f8c367b4-abb6-4a5d-8c56-12347439d3ee)
![Recommendation Page](https://github.com/user-attachments/assets/ff5ff947-848e-429e-b309-d344a0de0eb0)

## 🚀 Project Overview

This project helps users discover fashion products similar to the one they searched for. It uses **TF-IDF vectorization** and **cosine similarity** to find and recommend top matching products from a fashion dataset.

It’s built using:
- 🐍 Python
- 🔍 NLP (TF-IDF + Cosine Similarity)
- 🔥 Flask Web Framework
- 📊 Cleaned CSV Dataset of Fashion Items

---

## ✨ Features

- 🔎 Find products similar to your input
- 📁 Uses real-world fashion product dataset
- ⚡ Fast and accurate recommendations
- 🧠 Intelligent matching with `rapidfuzz` fuzzy search
- 💻 Simple and clean Flask API

---

## 🧠 How it Works

1. Combines `Category` and `Product` into one feature.
2. Applies **TF-IDF** vectorization on combined features.
3. Calculates **cosine similarity** between input and all products.
4. Uses **RapidFuzz** to get the closest product match from dataset.
5. Returns the **top 10 similar fashion products**.

---

## 🛠 Tech Stack

| Tech           | Description                             |
|----------------|-----------------------------------------|
| Python         | Main programming language               |
| Pandas         | Data manipulation                       |
| Flask          | Backend API & Web Server                |
| TfidfVectorizer| NLP vectorization of product features   |
| RapidFuzz      | Fuzzy string matching                   |
| Cosine Similarity | Similarity calculation between products |

---

## 📂 Dataset

Your dataset is in: `cleaned_fashion_product.csv`  
It contains:
- Category  
- Product Name  
- Combined Feature used for vectorization

---

## 🔮 Future Enhancements
- ✅ Add image-based product display

- ✅ Improve recommendations with deep learning (Word2Vec, BERT)

- ✅ Build full frontend using React or Bootstrap

- ✅ Deploy on Render / Vercel / Heroku

---

## 🤝 Author
👩‍💻 Developed with ❤️ by Yukti Nadhe
