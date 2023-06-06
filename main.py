from faker import Faker
import random
import pandas as pd

fake = Faker()

# Generate sample user profile data
num_profiles = 100
profiles = []

for _ in range(num_profiles):
    profile = {
        'Name': fake.name(),
        'Age': random.randint(18, 65),
        'Gender': random.choice(['Male', 'Female']),
        'Interests': random.sample(['Outdoor', 'Art', 'Food'], random.randint(1, 3)),
    }
    profiles.append(profile)

# Convert the profiles list to a Pandas DataFrame
df = pd.DataFrame(profiles)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Extract features from the interests column
vectorizer = CountVectorizer()
features = vectorizer.fit_transform(df['Interests'].apply(lambda x: ' '.join(x)))

# Compute the pairwise cosine similarity of feature vectors
similarity_matrix = cosine_similarity(features)

# Function to get recommendations based on user index
def get_recommendations(user_index, num_recommendations=5):
    user_similarities = similarity_matrix[user_index]
    most_similar_users = user_similarities.argsort()[-num_recommendations - 1:-1][::-1]
    return most_similar_users
