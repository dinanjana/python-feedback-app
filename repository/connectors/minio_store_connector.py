from minio import Minio
from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
                         BucketAlreadyExists)
import logging
import configs.connectors

# Initialize minioClient with an endpoint and access/secret keys.
minioClient = Minio(configs.connectors.MINIO_CONFIGS['MINIO_DB_URL'],
                    access_key=configs.connectors.MINIO_CONFIGS['ACCESS_KEY'],
                    secret_key=configs.connectors.MINIO_CONFIGS['SECRET_KEY'],
                    secure=True)

try:
    minioClient.make_bucket("logs", location=configs.connectors.MINIO_CONFIGS['BUCKET_LOCATION'])
except BucketAlreadyOwnedByYou as err:
    logging.warn(str(err))
    pass
except BucketAlreadyExists as err:
    logging.warn(str(err))
    pass
except ResponseError as err:
    logging.error(str(err))
    raise
