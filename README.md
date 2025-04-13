# 👗 Fashion Product Recommendation System

Welcome to the **Fashion Product Recommendation System** – a smart tool that suggests similar fashion products based on your input using Natural Language Processing and machine learning!

## Screenshorts

![image](https://github.com/user-attachments/assets/59cd997c-d714-4494-a692-9697d466867e)
![image](https://github.com/user-attachments/assets/b96c6199-cee9-43c9-8e0a-59252b7d5af2)


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
