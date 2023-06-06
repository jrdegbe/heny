from fastapi import FastAPI
from typing import List

app = FastAPI()

# API endpoint to get user profile by index
@app.get('/users/{user_index}')
def get_user_profile(user_index: int):
    if user_index < 0 or user_index >= len(df):
        return {'error': 'Invalid user index'}
    
    return df.loc[user_index].to_dict()

# API endpoint to get recommendations for a user by index
@app.get('/users/{user_index}/recommendations')
def get_user_recommendations(user_index: int, num_recommendations: int = 5):
    if user_index < 0 or user_index >= len(df):
        return {'error': 'Invalid user index'}
    
    recommendations = get_recommendations(user_index, num_recommendations)
    return [df.loc[recommendation].to_dict() for recommendation in recommendations]
