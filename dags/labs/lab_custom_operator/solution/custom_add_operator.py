from airflow.models.baseoperator import BaseOperator

class AddOperator(BaseOperator):

    def __init__(self,num1,num2,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.num1 = num1
        self.num2 = num2

    def execute(self,context):
        print(f'Addition of {self.num1} and {self.num2} is {self.num1+self.num2}')
        return self.num1+self.num2
