from flask import Flask, jsonify, request_started
import requests

app = Flask(__name__)
# Endpoint for getting user information
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Code to get user information using user_id
    user = {'name': 'Eugene ', 'age': 25, 'bio': 'Hello World!'}
    return jsonify(user)
# Endpoint for liking a user
@app.route('/like', methods=['POST'])
def like_user():
    # Code to like a user using user_id in request body
    user_id = request.json['user_id']
    return jsonify({'message': f'Liked user {user_id}!'})
# Endpoint for disliking a user
@app.route('/dislike', methods=['POST'])
def dislike_user():
    # Code to dislike a user using user_id in request body
    user_id = request.json['user_id']
    return jsonify({'message': f'Disliked user {user_id}!'})
if __name__ == '__main__':
    app.run(debug=True)