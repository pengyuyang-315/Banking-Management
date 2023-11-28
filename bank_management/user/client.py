from datetime import datetime

class client:
    
    total_number = 0
    def __init__(self,name,email,phoneNumber,balance,password):
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self._balance = balance
        self._password = password
        self.create_time = datetime.now()
        client.total_number +=1
    
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
    


# c1 = client("Annie","xx.com","12345",1000)
# c2 = client("Billy","yy.com","543221",1000)
# c1.transfer(500,c2)
# print(c1.show_information())
# print(c2.show_information())
