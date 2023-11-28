from user.client import client

def main():
    print("Welcome to AZYY Bank")
    role = int(input("Plz choose your role:1. I'm new to open accoun,2. Existing client,3. Admin,4. Investment Manager\n"))

    if role == 1:
        new_user_registration()
    elif role == 2:
        existing_user_login()
    elif role == 3:
        admin_login()
    elif role == 4:
        investment_manager_login()
    else:
        print("Invalid, run it again")

def new_user_registration():
    name = input("Plz input your name: ")
    phone = input("Plz input your phone number: ")
    initial_balance = float(input("Plz save your money: "))
    email = input("Plz input your email: ")
    password = input("plz input your password: ")

    c_new = client(name,email,phone,initial_balance,password)
    

def existing_user_login():
    # 在这里编写老用户登录的代码
    print("老用户登录功能暂未实现。")

def admin_login():
    # 在这里编写管理员登录的代码
    print("管理员登录功能暂未实现。")

def investment_manager_login():
    # 在这里编写基金管理员登录的代码
    print("基金管理员登录功能暂未实现。")

if __name__ == "__main__":
    main()
