from flask import Flask, request, jsonify
import hashlib


app = Flask(__name__)
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
    
# Recommenderer Service
class RecommendererService:
    def __init__(self):
        self.Recommenderes = {}
    def get_Recommender_details(self, Recommender_id):
        if Recommender_id in self.Recommenderes:
            return self.Recommenderes[Recommender_id]
        return None
    
# Recommendation Service
class RecommendationService:
    def get_recommendations(self, user_id):
        # return a collection of recommendations based on the user's preferences
        return [1, 2, 3, 4, 5]
    
    
# API Gateway Service
@app.route('/signup', methods=['POST'])
def signup():
    profile_service = ProfileService()
    username = request.json['username']
    password = request.json['password']
    result = profile_service.signup(username, password)
    return jsonify({'result': result})
@app.route('/login', methods=['POST'])
def login():
    profile_service = ProfileService()
    username = request.json['username']
    password = request.json['password']
    result = profile_service.login(username, password)
    return jsonify({'result': result})
@app.route('/session/<session_id>', methods=['GET'])
def get_connection_info(session_id):
    session_service = SessionService()
    result = session_service.get_connection_info(session_id)
    return jsonify({'result': result})
@app.route('/Recommender/<Recommender_id>', methods=['GET'])
def get_Recommender_details(Recommender_id):
    Recommenderer_service = RecommendererService()
    result = Recommenderer_service.get_Recommender_details(Recommender_id)
    return jsonify({'result': result})