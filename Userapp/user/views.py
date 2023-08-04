from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource
from Userapp import app, api
from flask_jwt_extended import jwt_required
from .controller import get_all_users, get_user, delete_user

# from Userapp.master.views import token_required

getAllUser = Blueprint('getAllUser', __name__)
getUser = Blueprint('getUser', __name__)


class GetAllUsers(Resource):
    @jwt_required()
    def get(self):
        print("US")
        datas = get_all_users()
        usersdata = []
        for data in datas:
            usersdata.append({
                "UserName": data["UserName"],
                "Password": data["Password"],
                "FullName": data["FullName"],
                "Gender": data["Gender"],

            })
        print(usersdata)

        print("hi")
        return make_response(jsonify({"users": usersdata}), 200)


class GetUser(Resource):
    @jwt_required()
    def get(self, username):
        print(username)
        datas = get_user(username)
        print(datas)
        # userdata = []
        # for data in datas:
        #     userdata.append({
        #         "UserName": data["UserName"],
        #         "Password": data["Password"],
        #         "FullName": data["FullName"],
        #         "Gender": data["Gender"],
        #
        #     })
        return make_response(jsonify({"users": datas}), 200)

    def put(self, username):
        data = delete_user(username)
        if data is True:
            return make_response(jsonify("Deleted User"), 200)
        else:
            return make_response(jsonify("UserName is not Exist"), 400)


api.add_resource(GetAllUsers, '/getAllUser')
api.add_resource(GetUser, '/getUser/<username>')
