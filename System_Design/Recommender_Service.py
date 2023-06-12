from flask import Flask, request, jsonify


app = Flask(__name__)
# Recommender Service
class RecommenderService:
    def __init__(self):
        self.Recommenderes = {}
    def add_Recommender(self, user1_id, user2_id):
        Recommender_id = len(self.Recommenderes) + 1
        self.Recommenderes[Recommender_id] = (user1_id, user2_id)
    def get_Recommender_details(self, Recommender_id):
        if Recommender_id in self.Recommenderes:
            return self.Recommenderes[Recommender_id]
        return None
    
# API Gateway Service
@app.route('/Recommender', methods=['POST'])
def add_Recommender():
    Recommender_service = RecommenderService()
    user1_id = request.json['user1_id']
    user2_id = request.json['user2_id']
    Recommender_service.add_Recommender(user1_id, user2_id)
    return jsonify({'result': 'Recommender added successfully'})
@app.route('/Recommender/<Recommender_id>', methods=['GET'])
def get_Recommender_details(Recommender_id):
    Recommender_service = RecommenderService()
    result = Recommender_service.get_Recommender_details(Recommender_id)
    return jsonify({'result': result})
if __name__ == '__main__':
    app.run(debug=True)