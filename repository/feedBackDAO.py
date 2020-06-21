from datetime import datetime
import repository.connectors.mongoDBConnector


async def add_feedback(feedback):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    print('1')
    print(feedback)
    return await repository.connectors.mongoDBConnector.db.insert_one({
        "id": str(timestamp),
        "feedBack": "\"" +feedback['feedBack'] + "\"",
    })


async def get_feedbacks():
    cursor = repository.connectors.mongoDBConnector.db.find({})
    items = await cursor.to_list(length=500)
    return items
