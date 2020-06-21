import repository.feedBackDAO


async def add_feedback(feedback):
    return await repository.feedBackDAO.add_feedback(feedback=feedback)

async def get_feedbacks():
    return await repository.feedBackDAO.get_feedbacks()
