from fastapi import FastAPI
from fetch_restaurant_data import fetch_restaurant_data, create_recommendations

app = FastAPI()

@app.get("/restaurants/{location}")
def get_recommendations(location: str):
    restaurants = fetch_restaurant_data(location)
    recommendations = create_recommendations(restaurants)
    return {"recommendations": recommendations.tolist()}
