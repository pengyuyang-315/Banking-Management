# from .user.client import client
from user.client import new_user_registration
from user.admin import admin
from user.client import client
from user.admin import admin_login
from user.client import existing_user_login


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

clients_dict = clients_initialization()
admins_dict = admins_initialization()


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
                personal_invest()
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


def personal_invest():
    print("personal invest")

def test():
    # ad =admin(12,12,12)
    # ad.show_client_detail(client1)
    # ad.edit_client_detail(client1,2,5555)
    # ad.show_client_detail(client1)
    admin_login()


if __name__ == "__main__":
    main()