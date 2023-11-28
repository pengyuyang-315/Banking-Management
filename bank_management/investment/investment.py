class investment:
    def __init__(self,rate):
        self.rate=rate
class mortgage(investment):
    def __init__(self,year,initial_payment):
        investment.__init__(self,rate)
        self.rate=rate
        self.P=initial_payment
        self.r=self.rate/12
        self.n=year

    def calculate_mortgage(self):
        payment=self.P*(self.r*pow((1+self.r),self.n))/pow((1+self.r),self.n)
        print("the monthly payment should be: ",payment)

class zero_coupon_bond(investment):
    def __init__(self,pv,year):
        investment.__init__(self)
        self.pv=pv
        self.n=year
    def calculate_fv(self):
        fv=pow((1+self.rate),n)*self.pv
        print("the fv of the zero-coupon bond is: ",fv)

    def calculate_YTM(self):
        print("the YTM of the zero coupon bond is: ", r)


class 





