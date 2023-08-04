from flask import Blueprint, request, jsonify, make_response
from flask_restful import Resource
from Userapp import app, api
from .controller import updatePassword
from flask_jwt_extended import jwt_required

udtpassword = Blueprint('udtpassword', __name__)


class UpdatePassword(Resource):
    def put(self, username):
        data = request.get_json()
        print(data)
        result = updatePassword(username, data)
        if result is True:
            return make_response(jsonify("Update Password Succesfully"), 200)
        else:
            return make_response(jsonify("Something Went Wrong"), 400)


api.add_resource(UpdatePassword, '/updatePassword/<username>')
