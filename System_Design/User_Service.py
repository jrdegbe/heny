from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
class User(Resource):
    def post(self):
        # Create a new user
        json_data = request.get_json(force=True)
        username = json_data['username']
        password = json_data['password']
        # Store the new user in the database
        # ...
        return {'message': 'User created'}, 201
api.add_resource(User, '/user')
if __name__ == '__main__':
    app.run(debug=True)  

    