from datetime import datetime
import repository.connectors.mongo_db_connector
import logging


async def add_feedback(feedback):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    logging.info('Inserting feedback' + str(feedback))
    return await repository.connectors.mongo_db_connector.feedbacks_collection.insert_one({
        "id": str(timestamp),
        "feedBack": feedback['feedBack'],
        "name": feedback['name'],
        "stars": feedback['stars']
    })


async def get_feedbacks():
    cursor = repository.connectors.mongo_db_connector.feedbacks_collection.find({})
    items = await cursor.to_list(length=500)
    return items


def add_log_file_location(log_file_location):
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    logging.info('Inserting log location' + str(log_file_location))
    return repository.connectors.mongo_db_connector.log_location_collection.insert_one({
        "id": str(timestamp),
        "location": log_file_location
    })
