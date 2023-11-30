from datetime import datetime
from client import client

class admin:
    def __init__(self,name,workNumber,password):
        self.name = name
        self.phoneNumber = workNumber
        self._password = password
        self.create_time = datetime.now()

    def show_client_detail():
