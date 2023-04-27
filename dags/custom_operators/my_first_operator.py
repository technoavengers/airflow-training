# import the operator to inherit from
from airflow.models.baseoperator import BaseOperator

class MyOperator(BaseOperator):

    # define the .__init__() method that runs when the DAG is parsed
    def __init__(self, name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    # define the .execute() method that runs when a task uses this operator.
    def execute(self, context):
        message = f"Hello {self.name}"
        return message