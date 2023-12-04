import os
import psycopg2
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

class CustomFileAndS3Sensor(BaseSensorOperator):
    """
    Waits for a file to exist and an SQL condition to be true.
    """

    @apply_defaults
    def __init__(self, filepath, s3_bucket, s3_conn_id, s3_key, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #TODO: Initialize parameters

    def poke(self, context):
        """
        Checks for file existence and SQL condition.
        """
        #TODO: Write code to check if file exists

        """
        Checks for file in S3.
        """
        self.log.info(f'Checking for existence of S3 file {s3_key} in s3 bucket: {self.s3_bucket}')
        #TODO: Create S3Hook using S3 connection id

        #TODO: Use S3Hook check_for_key API to check whether file exists in S3 bucket 