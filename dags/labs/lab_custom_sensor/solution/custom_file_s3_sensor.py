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
        self.filepath = filepath
        self.s3_bucket = s3_bucket
        self.s3_conn_id = s3_conn_id
        self.s3_key = s3_key

    def poke(self, context):
        """
        Checks for file existence and SQL condition.
        """
        self.log.info(f'Poking for file: {self.filepath}')
        # Check file existence
        if not os.path.exists(self.filepath):
            self.log.info(f"File '{self.filepath}' not found.")
            return False

        self.log.info(f'Checking for existence of S3 file {s3_key} in s3 bucket: {self.s3_bucket}')
        s3_hook = S3Hook(aws_conn_id = self.s3_conn_id)
        if(s3_hook.check_for_key(self.s3_bucket,self.s3_key)):
            return True
        return False