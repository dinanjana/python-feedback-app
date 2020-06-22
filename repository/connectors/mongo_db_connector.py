from motor.motor_asyncio import AsyncIOMotorClient

# connect to MongoDB

client = AsyncIOMotorClient("mongodb+srv://feddback:f33dback@feedback-jgfh3.mongodb.net/feedBacks?retryWrites=true&w=majority")

feedbacks_collection = client.get_database("feedBacks").get_collection("feedBacks")

log_location_collection = client.get_database("feedBacks").get_collection("logs")