from datetime import datetime

from .client import client
client1 = client("Billy","billy@gmail.com",123456,1000,123456)
class admin:
    def __init__(self,name,workNumber,password):
        self.name = name
        self.phoneNumber = workNumber
        self._password = password
        self.create_time = datetime.now()

    def show_client_detail(self,cl):
        information = cl.show_information()
        for i in information:
            print(i)

if __name__ == "__main__":
    ad =admin(12,12,12)
    ad.show_client_detail(client1)
