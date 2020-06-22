from datetime import datetime
import repository.file_uploader_dao

log_file_location=''


# Make a bucket with the make_bucket API call.
def init_log_file_upload():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    global log_file_location
    log_file_location = 'application' + str(timestamp) + '.log'
    repository.file_uploader_dao.init_log_file_uploader('logs/application.log', log_file_location)


def get_log_file_location():
    return log_file_location
