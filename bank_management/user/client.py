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
        print("Successfully saved!")
    
    def withdraw_money(self,amount):
        if self._balance<amount:
            print("Not enough balance")
        else:
            self._balance-=amount
            print("Successfully withdrew")

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
        


def new_user_registration():
    name = input("Plz input your name: ")
    phone = input("Plz input your phone number: ")
    initial_balance = float(input("Plz save your money: "))
    email = input("Plz input your email: ")
    password = input("plz input your password: ")

    c_new = client(name,email,phone,initial_balance,password)

    
    print("Welcome to be the member of this big family!")
    return c_new
