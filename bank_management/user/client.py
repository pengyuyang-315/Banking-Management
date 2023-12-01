from datetime import datetime

class client:
    
    def __init__(self,name,email,phoneNumber,balance,password):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self._balance = balance
        self._password = password
        self.create_time = datetime.now()
    
    def save_money(self,amount):
        self._balance += amount
        print(self.name,"Successfully saved!")
    
    def withdraw_money(self,amount):
        if self._balance<amount:
            print("Not enough balance")
        else:
            self._balance-=amount
            print(self.name,"Successfully withdrew")

    def transfer(self,amount,receiver):
        if(self._balance<amount):
            print("Not enough money")
        else:
            receiver.save_money(amount)
            print("Successfully transfer to",receiver.name)
            self.withdraw_money(amount)

    def show_information(self):
        information = [self.name,self.email,self.phoneNumber,self.create_time,self._balance]
        return information
    
    def edit_password(self,new_password):
        self._password = new_password
        

    def get_password(self):
        return self._password

def new_user_registration():
    name = input("Plz input your name: ")
    phone = input("Plz input your phone number: ")
    initial_balance = float(input("Plz save your money: "))
    email = input("Plz input your email: ")
    password = int(input("plz input your password: "))

    c_new = client(name,email,phone,initial_balance,password)

    
    print("Welcome to be the member of this big family!")
    return c_new

def existing_user_login(clients_dict):
    # existing_user_login
    client_name = input("plz entre your name:\n")
    client_current = clients_dict.get(client_name)
    if client_current is not None:
        password = int(input("plz entre your password\n"))
        if password != client_current.get_password():
            print("wrong password")
            existing_user_login()
        else:
            print("Welcome",client_current.name)
            return client_current
    else:
        print("Not existing")