# from .user.client import client
from user.client import new_user_registration
from user.admin import admin
from user.client import client
from user.admin import admin_login
from investment.investment import mortgage
from investment.investment import zero_coupon_bond
from investment.investment import government_bond
from investment.manage_investment import show_all_investment
from investment.manage_investment import recommendation_bond

def clients_initialization():
    # initialize clients
    client1 = client("Billy","billy@gmail.com",123456,1000,123456)
    client2 = client("Lilly","Lilly@gmail.com",123456,2000,123456)
    client3 = client("Sally","Sally@gmail.com",123456,3000,123456)
    clients_dict = {
        client1.name: client1,
        client2.name: client2,
        client3.name: client3
    }
    return clients_dict

def admins_initialization():
    #initialize admins
    admin1 = admin("admin1",123,123456)
    admin2 = admin("admin2",124,123456)
    admins_dict={
        admin1.workNumber: admin1,
        admin2.workNumber: admin2
    }
    return admins_dict

def mortgage_initialization():
    # initialize 
    mortgage1 = mortgage(0.03,5,5,2000)
    mortgage2 = mortgage(0.04,7,5,3000)
    mortgage3 = mortgage(0.05,8,10,4000)
    mortgage_dict = {
        "low risk mortgage": mortgage1,
        "mid risk mortgage": mortgage2,
        "high risk mortgage": mortgage3
    }
    return mortgage_dict

def zcb_initialization():
    # initialize 
    zcb1 = zero_coupon_bond(0.03,5,2000,5)
    zcb2 = zero_coupon_bond(0.06,10,3000,8)
    zcb_dict = {
        "low risk zcb": zcb1,
        "high risk zcb": zcb2
    }
    return zcb_dict

def gov_initialization():
    # initialize 
    gov1 = government_bond(0.03,5,2000,4,1)
    gov2 = government_bond(0.05,5,3000,5,1)
    gov3 = government_bond(0.05,6,2000,3,2)
    gov_dict = {
        "low risk government bond": gov1,
        "mid risk government bond": gov2,
        "high risk government bond": gov3

    }
    return gov_dict

def main():
    clients_dict = clients_initialization()
    admins_dict = admins_initialization()
    print("Welcome to AZYY Bank")
    role = int(input("Plz choose your role:\n1. I'm new to open account,2. Existing client,3. Admin,4. Investment Manager,5. Quit\n"))

    if role == 1:
        c_new = new_user_registration()
        clients_dict[c_new.name] = c_new
        main()
    elif role == 2:
        existing_user_login()
    elif role == 3:
        admin_login(admins_dict)
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

def investment_manager_login():
    # 在这里编写基金管理员登录的代码
    print("基金管理员登录功能暂未实现。")

def test():
    # ad =admin(12,12,12)
    # ad.show_client_detail(client1)
    # ad.edit_client_detail(client1,2,5555)
    # ad.show_client_detail(client1)
    admin_login()


if __name__ == "__main__":
    main()