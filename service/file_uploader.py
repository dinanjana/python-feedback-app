from datetime import datetime
from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)
import logging

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio('play.min.io',
                    access_key='Q3AM3UQ867SPQQA43P2F',
                    secret_key='zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG',
                    secure=True)


# Make a bucket with the make_bucket API call.
def init():
    logging.info('Initiating log file upload')
    try:
        minioClient.make_bucket("logs", location="us-east-1")
    except BucketAlreadyOwnedByYou as err:
        logging.warn(str(err))
        pass
    except BucketAlreadyExists as err:
        logging.warn(str(err))
        pass
    except ResponseError as err:
        logging.error(str(err))
        raise

    try:
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        minioClient.fput_object('logs', 'application'+str(timestamp)+'.log', 'logs/application.log')
    except ResponseError as err:
        print(err)