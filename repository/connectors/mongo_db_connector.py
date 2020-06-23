from motor.motor_asyncio import AsyncIOMotorClient
import configs.connectors

# connect to MongoDB

client = AsyncIOMotorClient(configs.connectors.MONGO_DB_URL)

feedbacks_collection = client.get_database("feedBacks").get_collection("feedBacks")

log_location_collection = client.get_database("feedBacks").get_collection("logs")