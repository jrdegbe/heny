import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

def create_recommendations(restaurants):
    df = pd.DataFrame(restaurants)
    # Select relevant features for recommendation
    features = ["name", "categories"]
    df = df[features]
    
    # Preprocess the text data
    df["categories"] = df["categories"].apply(lambda x: ", ".join(x))
    df["categories"] = df["categories"].str.lower()
    
    # Compute the TF-IDF matrix
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df["categories"])
    
    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    
    # Generate recommendations
    indices = pd.Series(df.index, index=df["name"]).drop_duplicates()
    recommendations = get_top_recommendations("Restaurant A", indices, cosine_sim)
    
    return recommendations

def get_top_recommendations(name, indices, cosine_sim):
    idx = indices[name]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Get top 5 recommendations (excluding the input restaurant)
    restaurant_indices = [i[0] for i in sim_scores]
    
    return df["name"].iloc[restaurant_indices]

if __name__ == "__main__":
    restaurants = fetch_restaurant_data("New York City")
    recommendations = create_recommendations(restaurants)
    print(recommendations)
