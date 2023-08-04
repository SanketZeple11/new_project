from Userapp import mongo
from flask import make_response, jsonify


def UserRegistration(user_data):
    print("hello")
    result = mongo.db.UserInfo.find_one({"UserName": user_data["UserName"]})
    print("j")
    print(result)
    if result is None:
        mongo.db.UserInfo.insert_one(
            {"UserName": user_data["UserName"], "Password": user_data["Password"], "FullName": user_data["FullName"],
             "Gender": user_data["Gender"], "isDeleted": "False"})
        print("Yes")
        return "Register Succesfull"
    else:
        return "Something Went Wrong"
        # return make_response(jsonify("Something Went Wrong"), 400)


def check_user(auth):
    result = mongo.db.UserInfo.find_one({"UserName": auth["UserName"], "Password": auth["Password"]})
    print(result)
    return result


#
def check_for_user(data):
    result = mongo.db.UserInfo.find_one({"_id": data["_id"]})
    print("True")
    return result


def check_for_username(auth):
    result = mongo.db.UserInfo.find_one({"UserName": auth["UserName"]})
    print("username")
    return result


def check_for_password(data):
    result = mongo.db.UserInfo.find_one({"Password": data["Password"]})
    print("password")
    return True
