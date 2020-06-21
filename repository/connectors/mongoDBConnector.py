#from pymongo import MongoClient

from motor.motor_asyncio import AsyncIOMotorClient

# connect to MongoDB

# client = MongoClient("mongodb+srv://feddback:f33dback@feedback-jgfh3.mongodb.net/feedBacks?retryWrites=true&w=majority")

client = AsyncIOMotorClient("mongodb+srv://feddback:f33dback@feedback-jgfh3.mongodb.net/feedBacks?retryWrites=true&w=majority")

db = client.get_database("feedBacks").get_collection("feedBacks")