import jwt
from flask import Blueprint, request, make_response, jsonify
from Userapp import app, api, jwt, mongo
from flask_restful import Resource, fields, marshal_with, reqparse
from .controller import UserRegistration, check_user, check_for_user
from functools import wraps
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, unset_jwt_cookies, \
    create_refresh_token

register = Blueprint('register', __name__)
login = Blueprint('login', __name__)
logout = Blueprint('logout', __name__)
refreshtoken = Blueprint('refresh', __name__)

post_parser = reqparse.RequestParser()
post_parser.add_argument("UserName", type=str, required=True, help="UserName is Required")
post_parser.add_argument("Password", type=int, required=True, help="Password is Required")
post_parser.add_argument("FullName", type=str, required=True, help="FullName is Required")
post_parser.add_argument("Gender", type=str, required=True, help="Gender is Required")


# #
# def token_required(f):
#     @wraps(f)
#     def decorator(*args, **kwargs):
#         token = request.args.get('token')
#         print(token)
#         # if not token:
#         #     token = request.headers['x-access-tokens']
#         # if not token:
#         #     return jsonify({'message': "A valis token is missing"})
#         try:
#             data = jwt.decode(token, app.config["JWT_SECRET_KEY"], algorithms=["HS256"])
#             data = check_for_user(data)
#         except:
#             return jsonify({'message': "Token is invalid"})
#         return f(data, *args, **kwargs)
#
#     return decorator
#

#
# user_fields = {
#     "UserName": fields.String,
#     "Password": fields.String,
#     "FullName": fields.String,
#     "Gender": fields.String
# }
#
# class SchemaValidater():
#     def __int__(self, response={}):
#         self.response = response
#
#     def isTrue(self):
#         errormessages = []
#         try:
#             username = self.response.get("UserName", None)
#             if username is None:
#                 raise Exception("Error")
#         except Exception as e:
#             errormessages.append("UserName is required")
#         return errormessages


class RegisterUser(Resource):
    # @marshal_with(user_fields)
    def post(self):
        print("hi")
        args = post_parser.parse_args()
        user_data = request.get_json()
        print(user_data)

        # _instance = SchemaValidater(response=user_data)
        # response = _instance.isTrue()
        # if len(response) > 0:
        #     result = {
        #         "Status": "error",
        #         "message": response
        #     }, 403
        #     return result
        # else:
        #     pass
        # username = user_data["UserName"]
        # password = user_data["Password"]
        # fullname = user_data["FullName"]PUT
        # gender = user_data["Gender"]
        print('-----user_data')
        print(user_data)
        result = UserRegistration(user_data)
        return make_response(jsonify(result), 200)


class UserLogin(Resource):
    def post(self):
        print("ok")
        auth = request.get_json()
        auth = check_user(auth)
        if auth is None:
            return make_response(jsonify({"msg": "Bad username or password"}), 401)
        print("yo")
        access_token = create_access_token(identity=auth["UserName"], fresh=True)
        refresh_token = create_refresh_token(identity=auth["UserName"])

        print(access_token)
        return jsonify({"message": "Log in Succesfully", "Refresh token": refresh_token, "access token": access_token,
                        "user_id": auth["UserName"]})

        # print(auth)
        # if not auth or not auth["UserName"] or not auth["Password"]:
        #     print("hi")
        #     return make_response(
        #         'Could not verify',
        #         401,
        #         {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        #     )
        # user = check_for_username(auth)
        # if not auth:
        #     return make_response(
        #         'Could not verify',
        #         401,
        #         {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
        #     )
        # pwd_result = check_for_password(auth)
        # if pwd_result is True:
        #     print("there is")
        #     # generates the JWT Token
        #     token = jwt.encode({
        #         'public_id': pwd_result.public_id,
        #         'exp': datetime.utcnow() + timedelta(minutes=30)
        #     }, app.config["JWT_SECRET_KEY"])
        #
        #     return make_response(jsonify({'token': token.decode('UTF-8')}), 201)
        #     # returns 403 if password is wrong
        # return make_response(
        #     'Could not verify',
        #     403,
        #     {'WWW-Authenticate': 'Basic realm ="Wrong Password !!"'}
        # )


class UserLogOut(Resource):
    def delete(self):
        response = jsonify({"msg": "logout successful"})
        unset_jwt_cookies(response)
        return response


class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        identity = get_jwt_identity()
        print(identity)
        access_token = create_access_token(identity=identity, fresh=False)
        return jsonify(new_access_token=access_token)


class HealthCheck(Resource):
    def get(self):
        print('Testing mongo connection')
        # result = list(mongo.db.UserInfo.find({}, {"_id": 0}))
        # print(result)
        print('---------------------------------')
        return jsonify({'health_check': True})


api.add_resource(HealthCheck, '/healthcheck')
api.add_resource(RegisterUser, '/signup')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogOut, '/logout')
api.add_resource(RefreshToken, '/refresh')
# app.register_blueprint(refreshtoken)
# app.register_blueprint(logout)
# app.register_blueprint(register)
# app.register_blueprint(login)

# if __name__ == "__main__":
#     app.run(debug=True)
