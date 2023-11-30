from .user.client import client
from .user.client import new_user_registration
from .user.admin import admin


# initialize clients
client1 = client("Billy","billy@gmail.com",123456,1000,123456)
client2 = client("Lilly","Lilly@gmail.com",123456,2000,123456)
client3 = client("Sally","Sally@gmail.com",123456,3000,123456)

clients_dict = {
    client1.name: client1,
    client2.name: client2,
    client3.name: client3
}

def main():
    print("Welcome to AZYY Bank")
    role = int(input("Plz choose your role:\n1. I'm new to open account,2. Existing client,3. Admin,4. Investment Manager,5. Quit\n"))

    if role == 1:
        c_new = new_user_registration()
        clients_dict[c_new.name] = c_new
        main()
    elif role == 2:
        existing_user_login()
    elif role == 3:
        admin_login()
    elif role == 4:
        investment_manager_login()
    elif role == 5:
        print("Bye!")
        return 
    else:
        print("Invalid, run it again")

def existing_user_login():
    # 在这里编写老用户登录的代码
    print("老用户登录功能暂未实现。")

def admin_login():
    # 在这里编写管理员登录的代码
    print("管理员登录功能暂未实现。")

def investment_manager_login():
    # 在这里编写基金管理员登录的代码
    print("基金管理员登录功能暂未实现。")

def test():
    ad =admin(12,12,12)
    ad.show_client_detail(client1)
