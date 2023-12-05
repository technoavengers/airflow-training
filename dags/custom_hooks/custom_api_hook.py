from airflow.hooks.base_hook import BaseHook
import requests

class CustomApiHook(BaseHook):
    def __init__(self, custom_api_conn_id):
        self.conn_id = custom_api_conn_id
        self.base_url = self.get_connection(custom_api_conn_id).host

    
    def get_data(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        response = requests.get(url)

        if response.status_code == 200:
            return response.json() # Assuming JSON response
        else:
            response.raise_for_status()


 