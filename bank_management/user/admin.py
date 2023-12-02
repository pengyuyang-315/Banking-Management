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
        columns = ["name","email","PhoneNumber","created_date","balance"]
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
    
def admin_login(admins_dict,clients_dict):
    workNumber = int(input("plz entre your Working Number: "))
    ad_temp = admins_dict.get(workNumber)
    #check password
    if ad_temp is not None:
        input_password = int(input("plz entre your password: "))
        if input_password == ad_temp.password:
            ad = admins_dict.get(workNumber)
            print(ad.name,"Successfully login")
            admin_operations(ad,clients_dict)
        else:
            print("Wrong password")
    else:
        print("Not existing")

def admin_operations(admin,clients_dict):
    operation_num =int(input("plz entre your operation number:\n 1. check client's detail 2. edit client's detail 3. quit\n"))
    if operation_num == 3:
        print("bye, admin")
        return
    elif operation_num ==1 or operation_num==2:
        client_name = input("plz entre the client's name:\n ")
        client_target = clients_dict.get(client_name)
        if client_target is not None:
            if operation_num == 1:
                admin.show_client_detail(client_target)
                admin_operations(admin,clients_dict)
            elif operation_num ==2:
                editNumber = int(input("plz entre number:\n 1.edit password 2.edit phone number 3.edit email\n"))
                if editNumber not in (1,2,3):
                    print("Invalid number")
                else:
                    new_detail = input("plz entre your edited detail:\n")
                    admin.edit_client_detail(client_target,editNumber,new_detail)
                    admin_operations(admin,clients_dict)
        else:
            print("Not existing/Wrong name")
            admin_operations(admin,clients_dict)

    else:
        print("Wrong number")

if __name__ == "__main__":
    ad =admin(12,12,12)
    ad.show_client_detail(client1)
