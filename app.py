import tornado.escape
import tornado.ioloop
import tornado.locks
import tornado.web
import os.path
import controllers.feedbacks
import service.file_uploader
from tornado.options import define, options, parse_command_line
import logging

logging.basicConfig(filename='logs/application.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


define("port", default=8888, help="run on the given port", type=int)
define("debug", default=True, help="run in debug mode")

def main():
    parse_command_line()
    app = tornado.web.Application(
        [
            (r"/feedbacks/", controllers.feedbacks.FeedbacksHandler),
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=options.debug,
    )
    app.listen(options.port)
    service.file_uploader.init_log_file_upload()
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()