import os
import psycopg2
from airflow.sensors.base_sensor_operator import BaseSensorOperator
from airflow.utils.decorators import apply_defaults

class CustomFileAndSQLSensor(BaseSensorOperator):
    """
    Waits for a file to exist and an SQL condition to be true.
    """

    @apply_defaults
    def __init__(self, filepath, sql_query, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filepath = filepath
        self.sql_query = sql_query

    def poke(self, context):
        """
        Checks for file existence and SQL condition.
        """
        self.log.info(f'Poking for file: {self.filepath}')
        # Check file existence
        if not os.path.exists(self.filepath):
            self.log.info(f"File '{self.filepath}' not found.")
            return False

        self.log.info(f'Checking SQL condition: {self.sql_query}')
        # Check SQL condition
        try:
            conn = psycopg2.connect(
                host='postgres',
                user='airflow',
                password='airflow'
            )
            cursor = conn.cursor()
            cursor.execute(self.sql_query)
            result = cursor.fetchone()[0] # Assuming SQL query returns a single value

            if result:
                self.log.info("SQL condition is True.")
                return True
            else:
                self.log.info("SQL condition is False.")
                return False

        except psycopg2.Error as e:
            self.log.error(f"Error executing SQL query: {e}")
            return False
        finally:
            cursor.close()
            conn.close()