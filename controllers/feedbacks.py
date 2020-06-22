import tornado.escape
import tornado.web
import service.feedback

class FeedbacksHandler(tornado.web.RequestHandler):
    async def get(self):
        messages = await service.feedback.get_feedbacks()
        self.render("index.html", messages=messages)


    """Post a new feedback."""

    async def post(self):
        message = {
            "feedBack": self.get_argument("body"),
            "name": self.get_argument("name"),
            "stars": self.get_argument("stars")
        }
        await service.feedback.add_feedback(feedback=message)
        message["html"] = tornado.escape.to_unicode(
            self.render_string("message.html", message=message)
        )
        self.write(message)


