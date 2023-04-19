# import the operator to inherit from
from airflow.models.baseoperator import BaseOperator


# define the class inheriting from an existing operator class
class MyOperator(BaseOperator):
    """
    Simple example operator that logs one parameter and returns a string saying hi.
    :param my_parameter: (required) parameter taking any input.
    """

    # define the .__init__() method that runs when the DAG is parsed
    def __init__(self, my_parameter, *args, **kwargs):
        # initialize the parent operator
        super().__init__(*args, **kwargs)
        # assign class variables
        self.my_parameter = my_parameter

    # define the .execute() method that runs when a task uses this operator.
    # The Airflow context must always be passed to '.execute()', so make
    # sure to include the 'context' kwarg.
    def execute(self, context):
        # write to Airflow task logs
        self.log.info(self.my_parameter)
        # the return value of '.execute()' will be pushed to XCom by default
        return "hi :)"