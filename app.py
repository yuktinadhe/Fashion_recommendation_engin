from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rapidfuzz import process

# Load dataset
df = pd.read_csv('cleaned_fashion_product.csv')  # Replace with your actual dataset file

# Precompute similarity
df['Combined_Feature'] = df['Category'] + ' ' + df['Product']
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(df['Combined_Feature'])
similarity = cosine_similarity(feature_vectors)

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Recommendation API
@app.route('/recommend', methods=['POST'])
def recommend():
    input_product = request.form.get('product')
    
    if not input_product:
        return jsonify({"error": "Please provide a product name"}), 400
    
    # Find the closest match
    database_products = df['Product'].tolist()
    find_match = process.extract(input_product, database_products)
    closest_match = find_match[0]
    index_of_product = closest_match[2]

    # Get similarity scores
    similarity_score = list(enumerate(similarity[index_of_product]))
    sorted_product_list = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    recommendations = []
    for i, (index, score) in enumerate(sorted_product_list[:10]):
        category = df.iloc[index]['Category']
        product = df.iloc[index]['Product']
        recommendations.append({"Category": category, "Product": product})

    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
