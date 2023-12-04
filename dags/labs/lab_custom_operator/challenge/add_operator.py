# import the operator to inherit from
from airflow.models.baseoperator import BaseOperator

class AddOperator(BaseOperator):

    # define the .__init__() method that runs when the DAG is parsed
    def __init__(self, num1, num2, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #TODO: Intialize parameters num1 and num2

    # define the .execute() method that runs when a task uses this operator.
    def execute(self, context):
        #TODO: Implement logic to add num1 and num2
        #TODO: Return the sum