import hashlib

# Profile Service
class ProfileService:
    def __init__(self):
        self.users = {}
    def signup(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = hashed_password
        return True
    def login(self, username, password):
        if username in self.users:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if self.users[username] == hashed_password:
                return True
        return False
    
# Session Service
class SessionService:
    def __init__(self):
        self.sessions = {}
    def get_connection_info(self, session_id):
        if session_id in self.sessions:
            return self.sessions[session_id]
        return None
    
# Recommender Service
class RecommenderService:
    def __init__(self):
        self.Recommend = {}
    def get_Recommend_details(self, Recommend_id):
        if Recommend_id in self.Recommendes:
            return self.Recommendes[Recommend_id]
        return None
    
# Recommendation Service
class RecommendationService:
    def get_recommendations(self, user_id):
        # return a collection of recommendations based on the user's preferences
        return [1, 2, 3, 4, 5]