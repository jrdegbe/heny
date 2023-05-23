import streamlit as st
import requests

API_URL = "http://localhost:8000"  # Update with your FastAPI server URL

def get_recommendations(location):
    url = f"{API_URL}/restaurants/{location}"
    response = requests.get(url)
    data = response.json()
    return data["recommendations"]

st.title("Restaurant Recommender")
location = st.text_input("Enter location:")
if st.button("Get Recommendations"):
    recommendations = get_recommendations(location)
    st.write(recommendations)
