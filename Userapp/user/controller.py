from Userapp import mongo


def get_all_users():
    result = mongo.db.UserInfo.find({"isDeleted": "False"}, {'_id': 0})
    print(result)
    return result


def get_user(username):
    result = mongo.db.UserInfo.find_one({"UserName": username, "isDeleted": "False"}, {"_id": 0, "isDeleted": 0})
    print(result)
    return result


def delete_user(username):
    result = mongo.db.UserInfo.update_one({"UserName": username}, {'$set': {"isDeleted": "True"}})
    return True
