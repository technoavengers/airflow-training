
from airflow.models.baseoperator import BaseOperator
from airflow.hooks.postgres_hook import PostgresHook

class MyPostgresOperator(BaseOperator):

    def __init__(self, post_conn_id,table,file, *args, **kwargs):
        # initialize the parent operator
        super().__init__(*args, **kwargs)
        # assign class variables
        self.post_conn_id = post_conn_id
        self.table= table
        self.file = file
    
    def execute(self, context):
        pg_hook = PostgresHook(postgres_conn_id=self.post_conn_id)
        pg_hook.bulk_dump(self.table, self.file)
        # the return value of '.execute()' will be pushed to XCom by default
        return "done"