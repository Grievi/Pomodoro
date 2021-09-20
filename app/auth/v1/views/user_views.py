from app.auth.v1.models.user_models import UserModels
from flask import request
from flask_restful import Resource
from flask_restful.reqparse import RequestParser

parser = RequestParser()

parser.add_argument("username", type=str, required=True, help="Enter your username")
parser.add_argument("worktime", type=str, required=True, help="Please Set Your Working time")
parser.add_argument("breaktime", type=str, required=True, help="Please Set Your break time duration")
parser.add_argument("breaktask", type=str, required=True, help="Enter the task you will do during break time")


class User(Resource):
    """
    User endpoints
    """

    def post(self):
        """
        register user endpoint
        """
        args = parser.parse_args()
        args = request.get_json()
        username = args["username"]
        password = args["password"]
        worktime = args["worktime"]
        breaktime = args ["breaktime"]
        breaktask = args["breaktask"]

        newUser = UserModels(username, password , worktime, breaktime, breaktask)
        newUser.save_user()

        return {"message": "User registered successfully",
                "user": newUser.__dict__},201

    def get(self):
        return{
            'user':UserModels.users
        }

class UserSearch(Resource):
    def get(self,id):
        user_id = int(id)-1

        return {
            'user': UserModels.users[user_id],
        }
            
