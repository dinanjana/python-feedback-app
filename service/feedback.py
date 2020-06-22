import repository.feedback_dao


async def add_feedback(feedback):
    return await repository.feedback_dao.add_feedback(feedback=feedback)

async def get_feedbacks():
    return await repository.feedback_dao.get_feedbacks()
