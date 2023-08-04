from Userapp import mongo


def updatePassword(username, data):
    result = mongo.db.UserInfo.find_one({"UserName": username})
    print(result)
    if result is None:
        return False
    else:
        pwd = mongo.db.UserInfo.update({"UserName": username}, {"$set": {"Password": data["Password"]}})
        print(pwd)
        return True
