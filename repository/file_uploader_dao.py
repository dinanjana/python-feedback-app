from minio.error import ResponseError
import logging
import repository.connectors.minio_store_connector


def init_log_file_uploader(log_file, uploaded_log_file):
    logging.info('Initiating log file upload')
    try:
        repository.connectors.minio_store_connector.minioClient.fput_object('logs', uploaded_log_file, log_file)
    except ResponseError as err:
        logging.error(str(err))
