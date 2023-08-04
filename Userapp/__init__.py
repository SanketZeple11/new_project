import os

from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from pymongo import MongoClient
from flask_jwt_extended import JWTManager
from datetime import datetime, timedelta

app = Flask(__name__)
# connection_String = "mongodb+srv://sanketzeple:root@cluster0.30jbnq4.mongodb.net/?retryWrites=true&w=majority"
# client = MongoClient('mongodb://localhost:27017/UserDB')
app.config['MONGO_URI'] = 'mongodb://mongo:27017/UserDB'
mongo = PyMongo(app)
print('Testing mongo connection')
# result = list(mongo.db.UserInfo.find({}, {"_id": 0}))
# print(result)
# print('---------------------------------')
# db = client["UserDB"]
# col = db["UserInfo"]

app.config["JWT_SECRET_KEY"] = "super_secret"
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies", "json", "query_string"]
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)
jwt = JWTManager(app)
api = Api(app)
