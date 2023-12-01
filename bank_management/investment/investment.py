class investment:
    def __init__(self,rate,risk):
        self.rate=rate
        self.risk=risk
class mortgage(investment):
    def __init__(self,rate,risk,year,initial_payment):
        investment.__init__(self,rate,risk)
        self.P=initial_payment
        self.r=self.rate/12
        self.n=year

    def calculate_mortgage(self):
        payment=self.P*(self.r*pow((1+self.r),self.n))/pow((1+self.r),self.n)
        print("the monthly payment should be: ",payment)
    def show_details(self):
        print("The information details are:")
        print("rate:",self.rate,", risk:",self.risk,", year:",self.n,", initial payment:",self.P)
    


class zero_coupon_bond(investment):
    def __init__(self,rate,risk,pv,year):
        investment.__init__(self,rate,risk)
        self.pv=pv
        self.n=year
    def calculate_fv(self):
        fv=pow((1+self.rate),self.n)*self.pv
        print("the fv of the zero-coupon bond is: ",fv)

    def calculate_YTM(self):
        print("the YTM of the zero coupon bond is: ", r)
    
    def show_details(self):
        print("The information details are:")
        print("rate:",self.rate,", risk:",self.risk,", year:",self.n,", present value:",self.pv)


class government_bond(investment):
    def __init__(self,rate,risk,face_value,year,annual_semiannual):
        investment.__init__(self,rate,risk)
        self.pv=face_value
        self.n=year
        self.f=annual_semiannual #annual is 1 and semi-annual is 2

    def calculate_coupon(self):
        if(self.f==1):
            payment=self.pv*self. rate
            print("the bond will be paid annual. The payment each time is: ",payment)
        elif(self.f==2):
            payment=self.pv*self.rate/2
            print("the bond will be paid semi-annual. The payment each time is: ",payment)
        else:
            print("wrong input in the annual/ semi-annual section. Government bond will only be paid in one of the 2 ways.")
        
    def show_details(self): #change function
        print("The information details are:")
        print("rate:",self.rate,", risk:",self.risk,", year:",self.n,", face value:",self.pv,", how many times will you be paid in a year:",self.f)

"""

invest_1=investment(0.05,1)
mortgage_1=mortgage(0.05,1,5,2000)
mortgage_1.calculate_mortgage()
z_c_b_1=zero_coupon_bond(0.05,1,500,5)
z_c_b_1.calculate_fv()
gov_b_1=government_bond(0.05,2,500,5,2)
gov_b_1.calculate_coupon()
"""


    





