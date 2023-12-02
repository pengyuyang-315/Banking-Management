import sys
import os

# Add the project's root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# from .user.client import client
from user.client import new_user_registration
from user.admin import admin
from user.client import client
from user.admin import admin_login
from user.client import existing_user_login
#from investment.start_invest import mortgage_initialization
#from investment.start_invest import zcb_initialization
#from investment.start_invest import gov_initialization
from investment.investment import investment
from investment.investment import mortgage
from investment.investment import zero_coupon_bond
from investment.investment import government_bond
from investment.manage_investment import edit_rate
from investment.manage_investment import edit_risk
from investment.manage_investment import show_all_investment
from investment.manage_investment import recommendation_bond
from investment.manage_investment import mortgage_initialization
from investment.manage_investment import zcb_initialization
from investment.manage_investment import gov_initialization

def clients_initialization():
    # initialize clients
    client1 = client("Billy","billy@gmail.com",123456,10000,123456)
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

def investment_initialization():
    investment_dict={
    }
    return investment_dict

clients_dict = clients_initialization()
admins_dict = admins_initialization()
#initialize investment
mortgage_dict=mortgage_initialization()
zcb_dict=zcb_initialization()
gov_dict=gov_initialization()
inv_dict=investment_initialization()




def main():
    
    print("Welcome to AZYY Bank")
    role = int(input("Plz choose your role:\n1. I'm new to open account,2. Existing client,3. Admin,4. Quit\n"))

    if role == 1:
        c_new = new_user_registration()
        clients_dict[c_new.name] = c_new
        
        main()
    elif role == 2:
        
        client_current = existing_user_login(clients_dict)
        if client_current is not None:
            operationNumber = int(input("plz entre your operation number:\n 1.save money 2.withdraw money 3.check personal information 4. transfer 5.personal investment\n"))
            if operationNumber == 1:
                money_amount = int(input("plz entre amount to save\n"))
                client_current.save_money(money_amount)
            elif operationNumber == 2:
                money_amount = int(input("plz entre amount to withdraw\n"))
                client_current.withdraw_money(money_amount)
            elif operationNumber == 3:
                information = client_current.show_information()
                columns = ["name","email","PhoneNumber","created_date","balance"]
                for info, column in zip(information, columns):
                    print(f"{column}: {info}")

            elif operationNumber == 4:
                receiver_name = input("plz entre the receiver's name:\n")
                receiver = clients_dict.get(receiver_name)
                if receiver is not None:
                    if receiver_name == client_current.name:
                        print("cannot transfer to yourself")
                    else:
                        amount = int(input("plz entre the amount you want to transfer\n"))
                        client_current.transfer(amount,receiver)
                else:
                    print("Not existing")
                print("transfer")
                # client_current.transfer()
            elif operationNumber == 5:
                
                personal_invest(client_current)
            else:
                print("Invalid number")
        main()
    elif role == 3:
        admin_login(admins_dict,clients_dict)
        main()
    elif role == 4:
        print("Bye!")
        return 
    else:
        print("Invalid, run it again")


def personal_invest(c_new):
    operation_inv = int(input("plz enter your operation number:\n 1.show your investment 2.show all investment avaliable 3.buy investment 4.recommend investment 5.check investment details \n"))
    if operation_inv==1:
        if inv_dict.get(c_new.name) is not None:
            print("Investment you have: ")
            #print(inv_dict.get(c_new.name))
            for i in inv_dict[c_new.name]:
                i.show_details()
        else: 
            print("Not avaliable. You have no investment")

    elif operation_inv==2:
        show_all_investment(mortgage_dict,zcb_dict,gov_dict)
    
    elif operation_inv==3:
        if inv_dict.get(c_new.name) is None:
            inv_dict[c_new.name]=[]
            
        buy_option=int(input("Which investment do you want to buy? 1.mortgage 2.zero coupon bond 3.government bond\n"))
        inside_option=int(input("Which number do you want to buy?"))
        if(buy_option==1):
            
            get_inv=mortgage_dict.get(inside_option)
            if c_new._balance>=get_inv.P:

                inv_dict[c_new.name].append(get_inv)
                c_new._balance=c_new._balance-get_inv.P
            else:
                print("Not enough balance")
            
         
        elif(buy_option==2):
            get_inv=zcb_dict.get(inside_option)
            if c_new._balance>=get_inv.pv:
                inv_dict[c_new.name].append(get_inv)
                c_new._balance=c_new._balance-get_inv.pv
            
            else:
                print("Not enough balance")

        elif(buy_option==3):
            get_inv=gov_dict.get(inside_option)
            if c_new._balance>=get_inv.pv:
                inv_dict[c_new.name].append(get_inv)
                c_new._balance=c_new._balance-get_inv.pv
            
            else:
                print("Not enough balance")
    elif operation_inv==4:
        risk=int(input("Please give your risk preference"))
        rate=int(input("Please give your rate preference"))
        type=int(input("Please give me the type of investment you want to buy. 1.mortgage 2.zcb 3.gov"))
        recommendation_bond(risk,rate,type,mortgage_dict,zcb_dict,gov_dict)

    elif operation_inv==5:
        type=int(input("Please give me the type of investment you want to buy. 1.mortgage 2.zcb 3.gov"))
        if type==1:
            use_dict=mortgage_dict
            choice_operation=int(input("which mortgage do you want to check, please enter a number"))
            type_operation=int(input("Do you want to 1.calculate mortgage 2.show details"))
            if type_operation==1:
                use_dict[choice_operation].calculate_mortgage()
            elif type_operation==2:
                use_dict[choice_operation].show_details()
        elif type==2:
            use_dict=zcb_dict
            choice_operation=int(input("which zero coupon bond do you want to check, please enter a number"))
            type_operation=int(input("Do you want to 1.calculate fv 2.calculate YTM 3.show details"))
            if type_operation==1:
                use_dict[choice_operation].calculate_fv()
            elif type_operation==2:
                use_dict[choice_operation].calculate_YTM()
            elif type_operation==3:
                use_dict[choice_operation].show_details()
        elif type==3:
            use_dict=gov_dict
            choice_operation=int(input("which government bond do you want to check, please enter a number"))
            type_operation=int(input("Do you want to 1.calculate coupon 2.show details"))
            if type_operation==1:
                use_dict[choice_operation].calculate_coupon()
            
            elif type_operation==2:
                use_dict[choice_operation].show_details()

   


        

    print("personal invest")

def test():
    # ad =admin(12,12,12)
    # ad.show_client_detail(client1)
    # ad.edit_client_detail(client1,2,5555)
    # ad.show_client_detail(client1)
    admin_login()


if __name__ == "__main__":
    main()