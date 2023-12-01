from datetime import datetime

from .client import client

client1 = client("Billy","billy@gmail.com",123456,1000,123456)
class admin:
    def __init__(self,name,workNumber,password):
        self.name = name
        self.workNumber = workNumber
        self.password = password
        self.create_time = datetime.now()

    def show_client_detail(self,cl):
        information = cl.show_information()
        columns = ["name","email","PhoneNumber","balance","created_date"]
        for info, column in zip(information, columns):
            print(f"{column}: {info}")
    

    # 1: password 2: phoneNumber 3. email
    def edit_client_detail(self,cl,optionNumber,new_one):

        if optionNumber == 1:
            cl.edit_password(new_one)
        elif optionNumber == 2:
            cl.phoneNumber = new_one
        elif optionNumber == 3:
            cl.email = new_one 
        
        print("Successfully Edited")
        return
    
def admin_login(admins_dict):
    workNumber = int(input("plz entre your Working Number: "))
    ad_temp = admins_dict.get(workNumber)
    #check password
    if ad_temp is not None:
        input_password = int(input("plz entre your password: "))
        if input_password == ad_temp.password:
            ad = admins_dict.get(workNumber)
            print(ad.name,"Successfully login")
        else:
            print("Wrong password")
    else:
        print("Not existing")
if __name__ == "__main__":
    ad =admin(12,12,12)
    ad.show_client_detail(client1)
